from packet import Packet

class GrounddamagePacket(Packet):
    
    def __init__(self, time=None, position=None):
        self.time = time
        self.position = position
    
    def writeToOutput(self, stream):
        stream.writeInt(self.time)
        self.position.writeToOutput(stream)
