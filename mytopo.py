#!/usr/bin/python

from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller, RemoteController
from mininet.log import setLogLevel, info
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.topo import Topo

class SimpleTopo(topo):
	def __init__(self):
		Topo.__init__(self)
		    
		h1 = self.addHost('h1', ip = '10.0.0.1/8', mac = '00:00:00:00:00:01')
		h2 = self.addHost('h2', ip = '10.0.0.2/8', mac = '00:00:00:00:00:02')
		h3 = self.addHost('h3', ip = '10.0.0.3/8', mac = '00:00:00:00:00:03')
		s1 = self.addSwitch('s1')
		
		self.addLink(h1,s1)
		self.addLink(h2,s1)
		self.addLink(h3,s1)
		
def Test():
	topo = SimpleTopo()
	net = Mininet(topo = topo, host = CPULimitedHost, link = TCLink)
	net.start()
  dumpNodeConnections(net.hosts)
  net.pingAll()
  h1,h2 = net.get('h1', 'h2')
  net.iperf((h1, h2))
  net.stop()
if  __name__ == '__main__':
	setLogLevel('info')
	Test()