from packet import Packet

class InvswapPacket(Packet):
    
    def __init__(self, time=None, position=None, slotObject1=None, slotObject2 = None):
        self.time = time
        self.position = position
        self.slotObject1 = slotObject1
        self.slotObject2 = slotObject2
    
    def writeToOutput(self, stream):
        stream.writeInt(self.time)
        self.position.writeToOutput(stream)
        self.slotObject1.writeToOutput(stream)
        self.slotObject2.writeToOutput(stream)
