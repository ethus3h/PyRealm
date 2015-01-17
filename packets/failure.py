from packet import Packet

class FailurePacket(Packet):
    
    def __init__(self, errorId=None, errorDescription=None):
        self.errorId = errorId
        self.errorDescription = errorDescription
    
    def writeToOutput(self, stream):
        self.errorId = stream.readInt()
        self.errorDescription = stream.readUTF()
