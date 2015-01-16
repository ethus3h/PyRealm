from client import *

class EventListener():

    def __init__(self, factory):
        self.client = factory
    
    def onPreConnect(self):
        pass

    def onConnect(self): # when the client actually connects
        pass

    def onDisconnect(self):
        pass

    def onLoad(self, mapinfo): # on mapinfo
        pass

    def onStatDataUpdate(self):
        pass

class TestListener(EventListener):

    def __init__(self, factory):
        self.factory = factory
    
    def onConnect(self):
        self.client = self.factory.protocolInstance
        self.client.hello()

    def onLoad(self, mapinfo):
        pass
