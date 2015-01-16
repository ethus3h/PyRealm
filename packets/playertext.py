from packet import Packet

class PlayershootPacket(Packet):
    
    def __init__(self, text=None):
        self.text = text
    
    def writeToOutput(self, stream):
        stream.writeUTF(self.text)
