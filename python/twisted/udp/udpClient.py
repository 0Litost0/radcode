from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class UdpClient(DatagramProtocol):

    def doSend(self):
        self.transport.connect("127.0.0.1", 14550)
        self.transport.write("?")

    def datagramReceived(self, data, (host, port)):
        print "Received %r" % data



udpclient = UdpClient()
reactor.listenUDP(0, udpclient)
reactor.callWhenRunning(udpclient.doSend)
reactor.run()
