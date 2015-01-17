from xml.dom.minidom import parse
import sys
import random
import math

packetClassDict = {}

def str_to_class(string):
    try:
        mod = __import__(string.lower()[0:-6])
        return getattr(mod, string)
    except Exception as e:
        print e
        return None

def isInitialized():
    return len(packetClassDict) != 0

def init(path):
    root = parse(path).getElementsByTagName("Packets")[0]
    for packet in root.getElementsByTagName("Packet"):
        className = packet.attributes["id"].value[0].upper() + packet.attributes["id"].value[1:].lower() + "Packet"
        clazz = str_to_class(className)
        packetClassDict[packet.attributes["type"].value] = clazz

def create(packetId):
    if not isInitialized():
        return None
    if isinstance(packetId, int):
        packetId = str(packetId)
    
    if packetClassDict[packetId] != None:
        return packetClassDict[packetId]()
    else:
        return None

class Packet():
    def __init__(self,id):
        self.id = id
    
    def getId(self):
        for k,v in packetClassDict.iteritems():
            if v:
                print v
                if isinstance(self,v):
                    return int(k)
        return None
