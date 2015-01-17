from packet import Packet

class InvresultPacket(Packet):
    
    def __init__(self, result=None):
        self.result = result
    
    def parseFromInput(self, stream):
        self.result = stream.readInt()
