
class MovePacket():
    def __init__(self, tickId=None, time=None, newPosition=None, records=None):
        self.tickId = tickId
        self.time = time
        self.newPosition = newPosition
        self.records = records

    def writeToOutput(self,stream):
        stream.writeInt(self.tickId)
        stream.writeInt(self.time)
        self.newPosition.writeToOutput(stream)
        stream.writeShort(len(self.records))
        for i in xrange(0,len(self.records)):
            self.records[i].writeToOutput(stream)
