# -*- coding: utf-8 -*-

from graphe import *
import sys
import math

class Scanner:

	def __init__(self):
		self.g = Graphe()

	def parseStations(self):
		'''Creation des noeuds du graphe avec coordonnees'''
		f = open("metro.txt", 'r')
		lignes = f.read().splitlines()
		f.close()

		counter = 0

		for ligne in lignes:

			if(ligne.strip() != ''): #Si la ligne n'est pas une ligne qu'avec des caractères inutiles

				if "###" not in ligne:

					list_values = ligne.split(":")

					counter = 1
					name, coordX, coordY = None, None, None

					for item in list_values: #Tuple d'une ligne
						if(item != '\n'):
							if(counter == 3):
								name = item
								counter += 1

							elif(counter == 4):
								coordX = float(item)
								counter += 1

							elif(counter == 5):
								coordY = float(item)
								counter += 1

								if(name != None and coordX != None and coordY != None):
									self.g.add_Station(name, coordX, coordY) #On ajoute que les stations avec des coordonnees
							
							else:
								counter += 1

	def parseSegments(self):
		'''Creation des arcs du graphe'''
		f = open("metro.txt",'r')
		lignes = f.read().splitlines()
		f.close()

		counter = 0

		for i in range(2, len(lignes) - 1): #Scan des lignes

			if(lignes[i].strip() != ''): #La ligne courante n'est pas vide

				if "###" not in lignes[i] and "###" not in lignes[i - 1]: 

					list_values_prec = lignes[i - 1].split(":") #LIGNE PRECEDENTE
					list_values = lignes[i].split(":") #LIGNE COURANTE
					longueurPrec = len(list_values_prec)
					longueurCourant = len(list_values)

					line, depart, arrivee = None, None, None
					nameDep, nameArr = None, None
					coordXDep, coordXArr = None, None
					coordYDep, coordYArr =  None, None
					tpsDep, tpsArr = None, None

					#Scan des elements d'une ligne 
					if(longueurPrec == longueurCourant):

						if(longueurCourant >= 3): #Recuperation de la ligne de metro
							line = list_values[0] ###### 1 variable globale assignée
							nameDep = list_values_prec[2] #Station precedente
							nameArr = list_values[2] #Station courante
							
							if "corr" in line or "": #Cas des correspondances a pied. On neglige les stations eponymes aux coord differentes
								#print("||| Corr. to add found")
								indexStationDep = self.g.index_station_grossier(nameDep) #Station precedente
								indexStationArr = self.g.index_station_grossier(nameArr) #Station courante
								if(indexStationDep != -1 and indexStationArr != -1): # On check que les stations existent et on les recupere
									depart = self.g.stations[indexStationDep] ###### 2 -
									arrivee = self.g.stations[indexStationArr] ###### 3 -
										
									self.g.add_Segment(line, depart, arrivee, None, None)################# Creation corr		

						if (longueurCourant >= 5): #Coord X cas funi et triviaux ON NE RENTRE PAS POUR LES CAS SANS COORDONNEES car counter jamais 4
							coordXDep = float(list_values_prec[3])
							coordXArr = float(list_values[3])
							coordYDep = float(list_values_prec[4])
							coordYArr = float(list_values[4])
								
							if longueurCourant <= 5: #Cas RER et funi
								indexStationDep = self.g.index_station_exact(nameDep, coordXDep, coordYDep) #Station precedente
								indexStationArr = self.g.index_station_exact(nameArr, coordXArr, coordYArr) #Station courante

								if(indexStationDep != -1 and indexStationArr != -1):
									depart = self.g.stations[indexStationDep] ###### 2
									arrivee = self.g.stations[indexStationArr] ###### 3

									self.g.add_Segment(line, depart, arrivee, None, None)################ Creation funi

						if(longueurCourant >= 7): #Cas metro

							tpsDep = float(list_values_prec[5])
							tpsArr = float(list_values[5])
							tpsDep = math.floor(tpsDep) * 3600 + (tpsDep - math.floor(tpsDep)) * 100 * 60 #Conversion en secondes
							tpsArr = math.floor(tpsArr) * 3600 + (tpsArr - math.floor(tpsArr)) * 100 * 60

							indexStationDep = self.g.index_station_exact(nameDep, coordXDep, coordYDep) #Station precedente
							indexStationArr = self.g.index_station_exact(nameArr, coordXArr, coordYArr)

							if(indexStationDep != -1 and indexStationArr != -1):
								#print("| Segment to add found")
								depart = self.g.stations[indexStationDep] ###### 2
								arrivee = self.g.stations[indexStationArr] ###### 3
								self.g.add_Segment(line, depart, arrivee, tpsDep, tpsArr)############### Creation segment trivial
	
	def linkEponymStations(self):
		for station1 in self.g.stations:
			for station2 in self.g.stations:
				if(station1.name == station2.name and station1.coordX != station2.coordX and station1.coordY != station2.coordY):
					# print("%s>>>%s" %(station1.name, station2.name))
					self.g.add_Segment("corr", station1, station2, None, None)

	def build_Vertices(self, mode):
		for station in self.g.stations:
			self.g.add_Vertex(station)
			#print (">> %s added as vertex <<" %(station.name))

		if "dist" in mode:
			for segment in self.g.segments:
				self.g.add_Arc(segment.stationDepart, segment.stationArrivee, segment.coutDist)
				#print(">>> [%s-%s] added as edge <<<" %(segment.stationDepart, segment.stationArrivee))
		elif "time" in mode:
			for segment in self.g.segments:
				self.g.add_Arc(segment.stationDepart, segment.stationArrivee, segment.coutDuree)



if __name__ == "__main__":

	s = Scanner()
	s.parseStations()
	#s.g.allStationsToString()
	s.parseSegments()
	#s.g.allSegmentsToString()
	s.linkEponymStations()
	s.g.linkSegmentsToStations() # Graphe modelisation ready a ce stade
	#s.g.allStationsToString()











