import math

class Location():

    def __init__(x=None,y=None):
        self.x = x
        self.y = y

    def writeToOutput(self, stream):
        stream.writeFloat(self.x)
        stream.writeFloat(self.y)
    
    def parseFromInput(self, stream):
        self.x = stream.readFloat()
        self.y = stream.readFloat()

    def distanceTo(self, loc2):
        dX = self.x-loc2.x
        dY = self.y-loc2.y
        return math.sqrt(dX**2+dY**2)
