class Arret:
    
    def __init__(self, line, sens, first, last):
        self.line = line
        self.sens = sens
        self.firstMetro = first
        self.lastMetro = last

    def toString(self):
        print ("Ligne %s - sens %s - Deb= %s - Fin=  %s" %(self.line, self.sens, self.firstMetro ,self.lastMetro))
