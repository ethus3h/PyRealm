from packet import Packet

class TradeacceptedPacket(Packet):
    
    def __init__(self, myOffer=None, yourOffer=None):
        if not myOffer:
            myOffer = []
        self.myOffer = myOffer
        if not yourOffer:
            yourOffer = []
        self.yourOffer = yourOffer
    
    def parseFromInput(self, stream):
        for i in xrange(0,stream.readShort()):
            self.myOffer.append(stream.readBoolean())

        for i in xrange(0,stream.readShort()):
            self.yourOffer.append(stream.readBoolean())
