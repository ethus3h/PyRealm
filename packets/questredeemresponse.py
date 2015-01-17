from packet import Packet

class QuestredeemresponsePacket(Packet):
    
    def __init__(self, ok=None, message=None):
        self.ok = ok
        self.message = message
    
    def parseFromInput(self, stream):
        self.ok = stream.readBoolean()
        self.message = stream.readUTF()
