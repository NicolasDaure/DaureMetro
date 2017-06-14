class Segment:

    def __init__(self, depart, arrivee, distance, duree):
        self.stationDepart=depart
        self.stationArrivee=arrivee
        self.coutDist=distance
        self.coutDuree=duree

    def toString(self):
    	print ("Cette arrete allant de %s a %s, mesure %fkm et dure %fminutes" %(self.stationDepart.name, self.stationArrivee.name, self.coutDist, self.coutDuree))
    	print " "