
class ClientstatPacket():
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

    def parseFromInput(self,stream):
        self.name = stream.readUTF()
        self.value = stream.readInt()
