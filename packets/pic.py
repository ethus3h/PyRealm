from packet import Packet

class PicPacket(Packet):
    
    def __init__(self, bitmapData=None):
        self.bitmapData = bitmapData
    
    def parseFromInput(self,stream):
        width = stream.readInt()
        height = stream.readInt()
        
        self.bitmapData = stream.readBytes(width*height*4)

        
