
from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
	def dataReceive(self,data):
		self.transport.write(data)

class EchoFactory(protocol.Factory):
	def buildProtocol(self, addr):
		print("listening....") 
		return Echo()

print("1")
reactor.listenTCP(8000, EchoFactory())
reactor.run()
print("2")

