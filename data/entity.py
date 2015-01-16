from statdata import StatData

class Entity():

    def __init__(loc=None,objectId=None,status=None):
        self.loc = loc
        self.objectId = objectId
        self.status = status

    def writeToOutput(self, stream):
        stream.writeFloat(self.x)
        stream.writeFloat(self.y)
    
    def parseFromInput(self, stream):
        self.objectId = stream.readInt()
        self.loc.parseFromInput(stream)

        length = stream.readShort()

        self.status = []

        for i in xrange(0,length):
            self.status.append(StatData().parseFromInput(stream))
