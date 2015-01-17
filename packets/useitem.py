from packet import Packet

class UseitemPacket(Packet):
    
    def __init__(self, time=None, slotObject=None, itemUsePos=None, useType=None):
        self.time = time
        self.slotObject = slotobject.SlotObject()
        self.itemUsePos = location.location()
        self.useType = useType
    
    def writeToOutput(self, stream):
        stream.writeInt(self.time)
        self.slotObject.writeToOutput(stream)
        self.itemUsePos.writeToOutput(stream)
        stream.writeByte(self.useType)
