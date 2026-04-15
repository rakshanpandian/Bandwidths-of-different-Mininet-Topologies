from mininet.topo import Topo

class BusTopo(Topo):
    def build(self, bw, n=4):
        switches = []
        for i in range(n):
            h = self.addHost(f'h{i+1}', ip=f'10.0.0.{i+1}')
            s = self.addSwitch(f's{i+1}')
            self.addLink(h, s,bw=100)
            switches.append(s)
        for i in range(n - 1):
            self.addLink(switches[i], switches[i+1],bw=bw)

class RingTopo(Topo):
    def build(self, bw, n=4):
        switches = []
        for i in range(n):
            h = self.addHost(f'h{i+1}', ip=f'10.0.0.{i+1}')
            s = self.addSwitch(f's{i+1}')
            self.addLink(h, s,bw=100)
            switches.append(s)
        for i in range(n - 1):
            self.addLink(switches[i], switches[i+1],bw=bw)
        self.addLink(switches[n-1], switches[0],bw=bw)

class TreeTopo(Topo):
    def build(self, bw, n=4):
        s_root = self.addSwitch('s_root')
        for i in range(n):
            h1=self.addHost(f'h{2*i+1}', ip=f'10.0.0.{2*i+1}')
            h2=self.addHost(f'h{2*i+2}', ip=f'10.0.0.{2*i+2}')
            s = self.addSwitch(f's{i+1}')
            self.addLink(s,h1,bw=100)
            self.addLink(h2,s,bw=100)
            self.addLink(s,s_root,bw=bw)
