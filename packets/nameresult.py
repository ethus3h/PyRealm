from packet import Packet

class NameresultPacket(Packet):
    
    def __init__(self, success=None, errorText=None):
        self.success = success
        self.errorText = errorText
    
    def parseFromInput(self, stream):
        self.success = stream.readBoolean()
        self.errorText = stream.readUTF()
