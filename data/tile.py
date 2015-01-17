
class Tile():

    def __init__(self,x=None,y=None,type=None):
        self.x = x
        self.y = y
        self.type = type

    def parseFromInput(self,stream):
        self.x = stream.readShort()
        self.y = stream.readShort()
        self.type = stream.readUnsignedShort()

    
