from packet import Packet

class CreateguildPacket(Packet):
    
    def __init__(self, name=None):
        self.name = name
    
    def writeToOutput(self, stream):
        stream.writeUTF(self.name)
