from packet import Packet
from data import tile, object

class UpdatePacket(Packet):
    
    def __init__(self, tiles=None,newObjs=None,drops=None):
        if not tiles:
            tiles = []
        if not newObjs:
            newObjs = []
        if not drops:
            drops = []
        self.tiles = tiles
        self.newObjs = newObjs
        self.drops = drops
    
    def parseFromInput(self, stream):

        for i in xrange(0,stream.readShort()):
            self.tiles.append(tile.Tile().parseFromInput(stream))

        for i in xrange(0,stream.readShort()):
            self.newObjs.append(object.Object().parseFromInput(stream))

        for i in xrange(0,stream.readShort()):
            self.drops.append(stream.readInt())
