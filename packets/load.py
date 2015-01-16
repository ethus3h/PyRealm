from packet import Packet

class LoadPacket(Packet):
    
    def __init__(self, charId=None, isFromArena=None):
        self.charId = charId
        self.isFromArena = isFromArena
    
    def writeToOutput(self, stream):
        stream.writeInt(self.charId)
        stream.writeBoolean(self.isFromArena)

