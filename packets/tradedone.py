from packet import Packet

class TradedonePacket(Packet):

    SUCCESS = 1
    FAILED = 0
    
    def __init__(self, code=None, description=None):
        self.code = code
        self.description = description
        
    
    def parseFromInput(self, stream):
        self.code = stream.readInt()
        self.description = stream.readUTF()
