from station import *
from segment import *
from vertex import *
from collections import defaultdict, deque

class Graphe:

	def __init__(self):
		'''Constructeur du graphe soit un ensemble d'arretes et noeuds'''
		self.stations = [] #Liste des stations pour l'affichage
		self.segments = []  #Liste des arretes pour l'affichage
		self.vertDictio = {}
		self.countVert = 0

	def __iter__(self):
		return iter(self.vertDictio.values())


	def add_Segment(self, line, depart, arrivee, timeDep, timeArr):
		'''Ajoute un segment a la liste de segments'''
		segToAdd = Segment(line, depart, arrivee)
		found = 0
		for segment in self.segments:
			if (segment.stationDepart == segToAdd.stationDepart and segment.stationArrivee == segToAdd.stationArrivee and segment.numLigne == segToAdd.numLigne):
				found = 1
				#print ("------!!!- [%s>%s] already added -!!!------" %(segToAdd.stationDepart.name, segToAdd.stationArrivee.name))
				break

		if(found == 0):
			segToAdd.set_Distance()
			
			if "corr" in segToAdd.numLigne:
				segToAdd.set_DureeAPied()
				# print("||| Correspondance segment created")

			elif "funi" in segToAdd.numLigne:
				segToAdd.set_DureeFuni()
				# print("|| Funicular segment created")

			elif timeDep == None and timeArr == None:
				segToAdd.set_DureeRER()
				# print("| Segment RER created")

			else:
				segToAdd.set_DureeMetro(timeDep, timeArr)
				# print("| Segment metro created")


			self.segments.append(segToAdd)
			#print("-----[%s>%s] added to graphe" %(segToAdd.stationDepart.name, segToAdd.stationArrivee.name))

	def add_Station(self, name, x, y):
		'''Ajoute une station a la liste de stations'''
		stationToAdd = Station(name, x, y)
		found = 0
		for station in self.stations:
			if (station.name == stationToAdd.name and station.coordX == stationToAdd.coordX and station.coordY == stationToAdd.coordY):
				found = 1
				#print "-!!!- Station [%s] already added to graphe -!!!-" %(stationToAdd.name)
				break

		if(found == 0):
			self.stations.append(stationToAdd)

	def add_Vertex(self, station):
		self.countVert += 1
		vertToAdd = Vertex(station)
		self.vertDictio[station] = vertToAdd
		return vertToAdd

	def add_Arc(self, origine, cible, cout = 0):
		if origine not in self.vertDictio:
			self.add_Vertex(origine) #Graphe oriente donc pas d'equivalent retour
		self.vertDictio[origine].add_Voisin(self.vertDictio[cible], cout)


	def linkSegmentsToStations(self):
		for station in self.stations: #Pour chaque objet station dans la liste des stations du graphe
			for segment in self.segments: #On balaye tous les segments du graphe
				if(segment.stationDepart == station): #Si la station de depart du segment correspond a la station courante
					station.segmentsSuiv.append(segment) #On l'ajoute a la liste des segments partants de la station
					#print("Segment added to [%s]" %(station.name))

	def index_station_grossier(self, name):
		'''Si la station est dans stations retourne son index, -1 sinon'''
		index = -1
		counter = 0
		found = False #Pour ne pas tout parcourir si la station est trouvee
		#print "Searching for %s" %name
		while found == False and  counter < len(self.stations):
			if (self.stations[counter].name == name):
				#print "Station found %s at %d:%d(searched %s)" %(station.name, station.coordX, station.coordY, name)
				found = True
				index = counter

			else:
				counter += 1

		return index

	def index_station_exact(self, name, X, Y):
		'''Si la station est dans stations retourne son index, -1 sinon'''
		index = -1
		counter = 0
		found = False #Pour ne pas tout parcourir si la station est trouvee
		#print "Searching for %s" %name
		while found == False and  counter < len(self.stations):
			if (self.stations[counter].name == name and self.stations[counter].coordX == X and self.stations[counter].coordY == Y):
				#print "Station found %s at %d:%d(searched %s)" %(station.name, station.coordX, station.coordY, name)
				found = True
				index = counter

			else:
				counter += 1

		return index


	def get_MoyenneVitesse(self):
		'''Retourne la moyenne des vitesses caculables sur le reseau'''
		somme = 0
		counter = 0

		while counter < len(self.segments):
			counter += 1
			somme += segments[counter].get_Vitesse()

		return somme / counter

	def get_Vertex(self, n):
		if n in self.vertDictio:
			return self.vertDictio[n]
		else:
			return None

	def get_Vertices(self):
		return self.vertDictio.keys()


	def allStationsToString(self):
		for station in self.stations:
			print("@@@@@@@@@@@@@@@@@@@@@@@")
			station.toString()

	def allSegmentsToString(self):
		for segment in self.segments:
			segment.toString()
