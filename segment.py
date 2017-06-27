from station import *
import math
# globIdAssigner = 0 # Createur d'identifiants de segments

vMetro = 0.247767812455
vPied = vMetro/21 #Vitesse d'un pieton en BLABLABLA/s
vFuni = vPied * 4 #Vitesse funiculaire
vRER = vMetro * 2.5 #Vitesse RER

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
    	print("|| %s: %s>>>%s (D = %f, T = %f)" %(self.numLigne, self.stationDepart.name, self.stationArrivee.name, self.coutDist, self.coutDuree))

    def setDistance(self):
    	'''Attribue la distance entre les deux points du segment'''
    	deltaX = self.stationDepart.coordX - self.stationArrivee.coordX
    	deltaY = self.stationDepart.coordY - self.stationArrivee.coordY
    	self.coutDist = math.sqrt(deltaX**2 + deltaY**2)

    def setDureeMetro(self, timeDep, timeArr):
    	self.coutDuree = timeArr - timeDep

    def setDureeAPied(self):
    	'''Attribue la duree d'un voyage sur le segment pour un trajet a pied'''
    	self.coutDuree = self.coutDist/vPied

    def setDureeFuni(self):
    	'''Attribue la duree d'un voyage sur le segment pour un trajet a pied'''
    	self.coutDuree = self.coutDist/vFuni
    def setDureeRER(self):
    	'''Attribue la duree d'un voyage sur le segment pour un trajet RER'''
    	self.coutDuree = self.coutDist/vRER

    def getVitesse(self):
    	'''Retourne la vitesse du moyen de transport sur le segment si les duree et distances sont affectees, -1 sinon'''
    	V = -1
    	if(self.coutDist != 0 and self.coutDuree != 0):
    		V = self.coutDist/self.coutDuree

    	return V


if __name__ == "__main__":

	s1 = Station("Raspail", 292, 289)
	s1.toString()
	s2 = Station("Vavin", 282, 300)
	s2.toString()
	
	seg = Segment("4", s1, s2)
	print(type(seg))
	seg.setDistance()

	dep = math.floor(0.49) * 3600 + (0.49 - math.floor(0.49)) * 100 * 60 #Conversion en secondes
	arr = math.floor(0.50) * 3600 + (0.50 - math.floor(0.50)) * 100 * 60

	seg.setDureeMetro(dep, arr)
	print("V = %f" %(seg.getVitesse()))
	seg.toString()
	#print("Vmetro = %f") %(seg.coutDist/seg.coutDuree)