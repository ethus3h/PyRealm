from packet import Packet

class FilePacket(Packet):
    
    def __init__(self, fileName=None, file = None):
        self.fileName = fileName
        self.file = file
    
    def parseFromInput(self, stream):
        self.fileName = stream.readUTF()
        self.file = stream.readUTFBytes(stream.readInt())
