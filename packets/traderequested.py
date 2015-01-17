from packet import Packet

class TraderequestedPacket(Packet):
    
    def __init__(self, name=None):
        self.name = name

    def parseFromInput(self, stream):
        self.name = stream.readUTF()
