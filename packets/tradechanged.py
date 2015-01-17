from packet import Packet

class TradechangedPacket(Packet):
    
    def __init__(self, offer=None):
        if not offer:
            offer = []
        self.offer = offer
    
    def parseFromInput(self, stream):
        for i in xrange(0,stream.readShort()):
            self.offer.append(stream.readBoolean())
