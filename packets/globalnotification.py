from packet import Packet

class GlobalnotificationPacket(Packet):
    
    def __init__(self, type=None, text=None):
        self.type = type
        self.text = text

    def parseFromInput(self, stream):
        self.type = stream.readInt()
        self.text = stream.readUTF()
