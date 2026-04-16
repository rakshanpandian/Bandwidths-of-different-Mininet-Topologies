import sys
from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from topos import BusTopo, RingTopo, TreeTopo
from mininet.link import TCLink
import time
def run():
    print("Select Topology: 1. Bus  2. Ring  3. Tree")
    choice = input("Enter 1, 2, or 3: ")
    print("Enter the Bandwidth Range you wish to give it.")
    bw=int(input("Enter a value: "))
    

    if choice == '1':
        topo = BusTopo(bw=bw)
    elif choice == '2':
        topo = RingTopo(bw=bw)
    else:
        topo = TreeTopo(bw=bw)

    net = Mininet(topo=topo,link=TCLink, controller=RemoteController, switch=OVSSwitch)
    net.start()
    CLI(net)
    net.stop()
    time.sleep(5)

if __name__ == '__main__':
    setLogLevel('info')
    run()
