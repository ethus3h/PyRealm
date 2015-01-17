from packet import Packet

class InvdropPacket(Packet):
    
    def __init__(self, slotObject=None):
        self.slotObject = slotObject
    
    def writeToOutput(self, stream):
        self.slotObject.writeToOutput(stream)
