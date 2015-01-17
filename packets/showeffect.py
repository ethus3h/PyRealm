from packet import Packet
from data import location

class ShoweffectPacket(Packet):
    
    def __init__(self, effectType=None, targetObjectId = None, pos1=None, pos2=None, color=None):
        self.effectType = effectType
        self.targetObjectId = targetObjectId
        if not pos1:
            pos1 = location.Location()
        if not pos2:
            pos2 = location.Location()
        self.pos1 = pos1
        self.pos2 = pos2
        self.color = color

    def parseFromInput(self,stream):
        self.effectType = stream.readUnsignedByte()
        self.targetObjectId = stream.readInt()
        self.pos1.parseFromInput(stream)
        self.pos2.parseFromInput(stream)
        self.color = stream.readInt()
