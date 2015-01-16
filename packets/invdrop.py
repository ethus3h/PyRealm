from packet import Packet

class GotoackPacket(Packet):
    
    def __init__(self, slotObject=None):
        self.slotObject = slotObject
    
    def writeToOutput(self, stream):
        self.slotObject.writeToOutput(stream)
