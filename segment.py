from station import *
import math
# globIdAssigner = 0 # Createur d'identifiants de segments

vPied = 70.79 #Vitesse d'un pieton A CORRIGER
vFuni = vPied * 3.5

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

    def setDistance(self):
    	'''Attribue la distance entre les deux points du segment'''
    	deltaX = self.stationDepart.coordX - self.stationArrivee.coordX
    	deltaY = self.stationDepart.coordY - self.stationArrivee.coordY
    	self.coutDist = math.sqrt(deltaX**2 + deltaY**2)

    def setDureeMetro(self, timeDep, timeArr):
    	'''Attribue la duree d'un voyage sur le segment pour un trajet metro'''
    	#timeDep = 3600 * math.floor(timeDep) + 60 * 100 *(timeDep - math.floor(timeDep))
    	#timeArr = 3600 * math.floor(timeArr) + 60 * 100 * (timeDep - math.floor(timeArr))
    	self.coutDuree = timeArr - timeDep # en secondes

    def setDureeAPied(self):
    	'''Attribue la duree d'un voyage sur le segment pour un trajet a pied'''
    	self.coutDuree = self.coutDist/vPied

    def setDureeFuni(self):
    	'''Attribue la duree d'un voyage sur le segment pour un trajet a pied'''
    	self.coutDuree = self.coutDist/vFuni

    def getVitesse(self):
    	'''Retourne la vitesse du moyen de transport sur le segment si les duree et distances sont affectees, -1 sinon'''
    	V = -1
    	if(self.coutDist != 0 and self.coutDuree != 0):
    		V = self.coutDist/self.coutDuree
    	
    	return V

   	def toString(self):
		print ("L%s: %s -> %s (D=%f km, T=%f)" %(self.numLigne, self.stationDepart.name, self.stationArrivee.name, self.coutDist, self.coutDuree))

if __name__ == "__main__":

	s1 = Station("Raspail", 292, 289)
	s1.toString()
	s2 = Station("Vavin", 282, 300)
	s2.toString()
	seg = Segment("4", s1, s2)
	seg.setDistance()
	seg.setDureeMetro(0.49, 0.50)
	seg.toString()
	print("Vmetro = %f") %(seg.coutDist/seg.coutDuree)