from packet import Packet

class SetconditionPacket(Packet):
    
    def __init__(self, conditionEffect=None, conditionDuration=None):
        self.conditionEffect = conditionEffect
        self.conditionDuration = conditionDuration
    
    def writeToOutput(self, stream):
        stream.writeByte(self.conditionEffect)
        stream.writeFloat(self.conditionDuration)
