from packet import Packet

class BuyresultPacket(Packet):
    
    def __init__(self, result=None, resultString = None):
        self.result = result
        self.resultString = resultString
    
    def parseFromInput(self, stream):
        self.result = stream.readInt()
        self.resultString = stream.readUTF()
