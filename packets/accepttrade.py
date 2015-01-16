from packet import Packet

class AccepttradePacket(Packet):
    
    def __init__(self, myOffer=None, yourOffer = None):
        self.myOffer = myOffer
        self.yourOffer = yourOffer
    
    def writeToOutput(self, stream):
        stream.writeShort(len(self.myOffer))
        for i in xrange(0,len(self.myOffer)):
            stream.writeBoolean(self.myOffer[i])

        stream.writeShort(len(self.yourOffer))
        for i in xrange(0,len(self.yourOffer)):
            stream.writeBoolean(self.yourOffer[i])
