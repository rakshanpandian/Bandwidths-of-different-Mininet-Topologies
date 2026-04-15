from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet, ethernet, ipv4
from ryu.lib import stplib  # Import the STP library
from ryu.lib import dpid as dpid_lib

class RyuController(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
    
    # Define contexts so Ryu knows to load the STP module alongside this app
    _CONTEXTS = {'stplib': stplib.Stp}

    def __init__(self, *args, **kwargs):
        super(RyuController, self).__init__(*args, **kwargs)
        self.mac_to_port = {}
        self.stp = kwargs['stplib']

        # Optional: Set bridge priority (lower value = root bridge)
        # s1 will be the root of the tree/ring/bus
        config = {dpid_lib.str_to_dpid('0000000000000001'): {'bridge_priority': 0x8000}}
        self.stp.set_config(config)

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        parser = datapath.ofproto_parser
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(datapath.ofproto.OFPP_CONTROLLER, datapath.ofproto.OFPCML_NO_BUFFER)]
        self.add_flow(datapath, 0, match, actions)

    def add_flow(self, datapath, priority, match, actions):
        inst = [datapath.ofproto_parser.OFPInstructionActions(datapath.ofproto.OFPIT_APPLY_ACTIONS, actions)]
        mod = datapath.ofproto_parser.OFPFlowMod(datapath=datapath, priority=priority, match=match, instructions=inst)
        datapath.send_msg(mod)

    # IMPORTANT: Use stplib.EventPacketIn instead of ofp_event.EventOFPPacketIn
    # This ensures STP logic processes the packet before your forwarding logic
    @set_ev_cls(stplib.EventPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        in_port = msg.match['in_port']

        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocols(ethernet.ethernet)[0]
        
        # Scenario: Block 10.0.0.1 (h1) to 10.0.0.3 (h3)
        ip_pkt = pkt.get_protocol(ipv4.ipv4)
        if ip_pkt:
            if ip_pkt.src == '10.0.0.1' and ip_pkt.dst == '10.0.0.3':
                self.logger.info("DROPPED: Filtered packet from %s to %s", ip_pkt.src, ip_pkt.dst)
                match = parser.OFPMatch(eth_type=0x0800, ipv4_src='10.0.0.1', ipv4_dst='10.0.0.3')
                self.add_flow(datapath, 10, match, [])
                return

        # Simple Learning Switch Logic
        self.mac_to_port.setdefault(datapath.id, {})
        self.mac_to_port[datapath.id][eth.src] = in_port
        
        # Decide out_port
        if eth.dst in self.mac_to_port[datapath.id]:
            out_port = self.mac_to_port[datapath.id][eth.dst]
        else:
            out_port = ofproto.OFPP_FLOOD

        actions = [parser.OFPActionOutput(out_port)]

        # Install a flow to avoid PacketIn next time for this specific path
        if out_port != ofproto.OFPP_FLOOD:
            match = parser.OFPMatch(in_port=in_port, eth_dst=eth.dst, eth_src=eth.src)
            self.add_flow(datapath, 1, match, actions)

        # Send the packet out
        out = parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id,
                                  in_port=in_port, actions=actions, data=msg.data)
        datapath.send_msg(out)
