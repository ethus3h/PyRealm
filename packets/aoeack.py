from packet import Packet

class AoeackPacket(Packet):
    
    def __init__(self, time=None, position=None):
        self.time = time
        self.position = position
    
    def writeToOutput(self, stream):
        stream.writeInt(self.time)
        self.position.writeToOutput(stream)

    def parseFromInput(self, stream):
        self.time = stream.readInt()
        self.position.parseFromInput(stream)
