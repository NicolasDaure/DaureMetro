from arret import *

class Station:

    def __init__(self, name, x, y):
        self.name = name
        self.coordX=x
        self.coordY=y
        self.arret=[]
        self.correspondance=[]

    def addCorrespondance(self, c):
    	found=0
    	for corr in self.correspondance:
            if (corr==c):
                found=1
                print "Correspondance %s already added for %s" %(corr.name, c.name)
                break
    	if(found==0):
    		self.correspondance.append(c)

    def addArret(self, line, sens, first, last):
    	a=Arret(line, sens, first, last)
    	self.arret.append(a)

    def toString(self):
    	print ("Station %s at x=%d and y=%d" %(self.name , self.coordX ,self.coordY))
    	for arret in self.arret:
    		 arret.toString()
    	if(len(self.correspondance)!=0):
	    	print ("Correspondances of station : %s") %self.name
	    	for corr in self.correspondance:
	    		print corr.name
	   	print " "