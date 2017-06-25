# globIdAssigner = 0 # Créateur d'identifiants de segments

class Segment:

    def __init__(self, line, depart, arrivee, distance, duree):
    	# self.idSegment = globIdAssigner
    	# global globIdAssigner
    	# globIdAssigner += 1

    	self.numLigne = line #num de la ligne courante 
        self.stationDepart = depart #obj Station
        self.stationArrivee = arrivee #obj Station
        self.coutDist = distance
        self.coutDuree = duree

    def toString(self):
    	print ("L%: %s -> %s (D=%f km, T=%f min)" %(self.numLigne, self.stationDepart.name, self.stationArrivee.name, self.coutDist, self.coutDuree))
