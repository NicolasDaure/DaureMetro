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

	def set_Distance(self):
		'''Attribue la distance entre les deux points du segment'''
		deltaX = self.stationDepart.coordX - self.stationArrivee.coordX
		deltaY = self.stationDepart.coordY - self.stationArrivee.coordY
		self.coutDist = math.sqrt(deltaX**2 + deltaY**2)

	def set_DureeMetro(self, timeDep, timeArr):
		self.coutDuree = timeArr - timeDep

	def set_DureeAPied(self):
		'''Attribue la duree d'un voyage sur le segment pour un trajet a pied'''
		self.coutDuree = self.coutDist/vPied

	def set_DureeFuni(self):
		'''Attribue la duree d'un voyage sur le segment pour un trajet a pied'''
		self.coutDuree = self.coutDist/vFuni
		
	def set_DureeRER(self):
		'''Attribue la duree d'un voyage sur le segment pour un trajet RER'''
		self.coutDuree = self.coutDist/vRER

	def get_Distance(self):
		return self.coutDist

	def get_Vitesse(self):
		'''Retourne la vitesse du moyen de transport sur le segment si les duree et distances sont affectees, -1 sinon'''
		V = -1
		if(self.coutDist != 0 and self.coutDuree != 0):
			V = self.coutDist/self.coutDuree

		return V


if __name__ == "__main__":

	s1 = Station("Raspail", 292, 289)
	#s1.toString()
	s2 = Station("Vavin", 282, 300)
	#s2.toString()
	
	seg = Segment("14", s1, s2)
	seg.set_Distance()

	dico = {}
	dico[s1] = seg.get_Distance()

	print(dico)
	print(dico.keys()[0].name)


	




