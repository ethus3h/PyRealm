from statdata import StatData

class Status():

    def __init__(loc=None,objectId=None,status=None):
        self.loc = loc
        self.objectId = objectId
        self.status = status

    def writeToOutput(self, stream):
        stream.writeInt(self.objectId)
        self.loc.writeToOutput(stream)

        stream.writeShort(len(self.status))
        for i in xrange(0,len(self.status)):
            self.status[i].writeToOutput(stream)
    
    def parseFromInput(self, stream):
        self.objectId = stream.readInt()
        self.loc.parseFromInput(stream)

        self.status = []

        for i in xrange(0,stream.readShort()):
            self.status.append(StatData().parseFromInput(stream))
