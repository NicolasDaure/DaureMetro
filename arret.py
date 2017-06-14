class Arret:

    def __init__(self, line, sens, first, last):
    	self.line=line
    	self.sens=sens
        self.firstMetro=first
        self.lastMetro=last

    def toString(self):
    	print ("Ligne %s, sens %s, starting at %s and ending at %s" %(self.line, self.sens, self.firstMetro ,self.lastMetro))