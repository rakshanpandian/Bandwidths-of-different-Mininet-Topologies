from mininet.topo import Topo
from mininet.link import TCLink
class BusTopo(Topo):
    def build(self, bw, n=4):
        switches = []
        for i in range(n):
            h = self.addHost(f'h{i+1}', ip=f'10.0.0.{i+1}')
            s = self.addSwitch(f's{i+1}')
            self.addLink(h, s,cls=TCLink,bw=bw)
            switches.append(s)
        for i in range(n - 1):
            self.addLink(switches[i], switches[i+1],cls=TCLink,bw=bw)

class RingTopo(Topo):
    def build(self, bw, n=4):
        switches = []
        for i in range(n):
            h = self.addHost(f'h{i+1}', ip=f'10.0.0.{i+1}')
            s = self.addSwitch(f's{i+1}')
            self.addLink(h, s,cls=TCLink,bw=bw)
            switches.append(s)
        for i in range(n - 1):
            self.addLink(switches[i], switches[i+1],cls=TCLink,bw=bw)
        self.addLink(switches[n-1], switches[0],cls=TCLink, bw=bw)

class TreeTopo(Topo):
    def build(self, bw, n=4):
        s_root = self.addSwitch('s0')
        for i in range(n):
            h1=self.addHost(f'h{2*i+1}', ip=f'10.0.0.{2*i+1}')
            h2=self.addHost(f'h{2*i+2}', ip=f'10.0.0.{2*i+2}')
            s = self.addSwitch(f's{i+1}')
            self.addLink(s,h1,cls=TCLink,bw=bw)
            self.addLink(s,h2,cls=TCLink,bw=bw)
            self.addLink(s,s_root,cls=TCLink,bw=bw)
