from statdata import StatData

class Object():

    def __init__(objectType=None,status=None):
        self.objectType = objectType
        self.status = status
    
    def parseFromInput(self, stream):
        self.objectType = stream.readShort()
        self.status.parseFromInput(stream)
