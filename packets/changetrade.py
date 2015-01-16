from packet import Packet

class ChangetradePacket(Packet):
    
    def __init__(self, offer=None):
        self.offer = offer
    
    def writeToOutput(self, stream):
        stream.writeShort(len(self.offer))
        for i in xrange(0,len(self.offer)):
            stream.writeBoolean(self.offer[i])
