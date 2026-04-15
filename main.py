import sys
from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from topos import BusTopo, RingTopo, TreeTopo

def run():
    print("Select Topology: 1. Bus  2. Ring  3. Tree")
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        topo = BusTopo()
    elif choice == '2':
        topo = RingTopo()
    else:
        topo = TreeTopo()

    net = Mininet(topo=topo, controller=RemoteController, switch=OVSSwitch)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
