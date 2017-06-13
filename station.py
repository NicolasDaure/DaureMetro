from arret import *

class Station:

    def __init__(self, name, x, y):
        self.name = name
        self.coordX=x
        self.coordY=y
        self.arret=[]

    def addArret(self, line, sens, first, last):
    	a=Arret(line, sens, first, last)
    	self.arret.append(a)

    def toString(self):
    	print ("Station %s at x=%d and y=%d" %(self.name , self.coordX ,self.coordY))
    	for arret in self.arret:
    		 arret.toString()
    	print " "