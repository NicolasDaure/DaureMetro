from station import *
import math
# globIdAssigner = 0 # Createur d'identifiants de segments

class Segment:

    def __init__(self, line, depart, arrivee):
    	# self.idSegment = globIdAssigner
    	# global globIdAssigner
    	# globIdAssigner += 1

    	self.numLigne = line #num de la ligne courante 
        self.stationDepart = depart #obj Station
        self.stationArrivee = arrivee #obj Station
        self.coutDist = 0 #computeDistance(self.stationDepart, self.StationArrivee)
        self.coutDuree = 0

    def toString(self):
    	print ("L%s: %s -> %s (D=%f km, T=%f min)" %(self.numLigne, self.stationDepart.name, self.stationArrivee.name, self.coutDist, self.coutDuree))

    # def computeDistance(station1, station2):
    # 	deltaXcarr = (station1.coordX - station2.coordX)**2
    # 	deltaYcarr = (station1.coordY - station2.coordY)**2

    # 	return math.sqrt(deltaXcarr + deltaYcarr)

if __name__ == "__main__":

	s1 = Station("La Defense", 77, 465)
	s1.toString()
	s2 = Station("Esplanade de la Defense", 91, 461)
	s2.toString()
	seg = Segment("1", s1, s2)
	seg.toString()