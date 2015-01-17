from packet import Packet

class ReconnectPacket(Packet):
    
    def __init__(self, name=None, host=None, port=None, gameId=None, keyTime=None, key=None, isFromArena=None):
        self.name = name
        self.host = host
        self.port = port
        self.gameId = gameId
        self.keyTime = keyTime
        if not key:
            key = []
        self.key = key
        self.isFromArena = isFromArena

    
    def parseFromInput(self, stream):
        self.name = stream.readUTF()
        self.host = stream.readUTF()
        self.port = stream.readInt()
        self.gameId = stream.readInt()
        self.keyTime = stream.readInt()
        self.isFromArena = stream.readBoolean()
        self.key = stream.read(stream.readShort())
