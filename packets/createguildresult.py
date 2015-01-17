from packet import Packet

class CreateguildresultPacket(Packet):
    
    def __init__(self, success=None, lineBuilderJson=None):
        self.success = success
        self.lineBuilderJson = lineBuilderJson
    
    def parseFromInput(self, stream):
        self.success = stream.readBoolean()
        self.lineBuilderJson = stream.readUTF()
