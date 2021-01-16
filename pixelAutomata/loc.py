# -*- coding: utf-8 -*-

bounded = True
from lim import xLim
from lim import yLim

class coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getNW(self):
        return coords(self.x-1,self.y+1)
    def getN(self):
        return coords(self.x,self.y+1)
    def getNE(self):
        return coords(self.x+1,self.y+1)
    def getE(self):
        return coords(self.x+1,self.y)
    def getSE(self):
        return coords(self.x+1,self.y-1)
    def getS(self):
        return coords(self.x,self.y-1)
    def getSW(self):
        return coords(self.x-1,self.y-1)
    def getW(self):
        return coords(self.x-1,self.y)

class bcoords:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getNW(self):
        return coords((self.x-1)%xLim,(self.y+1)%yLim)
    def getN(self):
        return coords(self.x,(self.y+1)%yLim)
    def getNE(self):
        return coords((self.x+1)%xLim,(self.y+1)%yLim)
    def getE(self):
        return coords((self.x+1)%xLim,self.y)
    def getSE(self):
        return coords((self.x+1)%xLim,(self.y-1)%yLim)
    def getS(self):
        return coords(self.x,(self.y-1)%yLim)
    def getSW(self):
        return coords((self.x-1)%xLim,(self.y-1)%yLim)
    def getW(self):
        return coords((self.x-1)%xLim,self.y)

class loc:
    def __init__(self,coords):
        self.coords = coords
        self.state = False
        