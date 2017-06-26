# -*- coding: utf-8 -*-

from graphe import *
import sys

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
									self.g.addStation(name, coordX, coordY) #On ajoute que les stations avec des coordonnees

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
					list_values = lignes[i].split(":") # LIGNE COURANTE

					counter = 0
					line, depart, arrivee = None, None, None
					nameDep, nameArr = None, None
					coordXDep, coordXArr = None, None
					coordYDep, coordYArr =  None, None
					tpsDep, tpsArr = None, None

					#Scan des elements d'une ligne 
					for item in list_values: #Tuple de la ligne courante
						if(item != '\n'):
							if(counter == 1): #Recuperation de la ligne de metro
								line = item ###### 1
								counter += 1

							if(counter == 3): # Recuperation des noms des stations concernees
								nameDep = list_values_prec[counter] #Station precedente
								nameArr = list_values[counter] #Station courante
								counter += 1

								if "coor" in line: #Cas des correspondances a pied. On neglige les stations eponymes aux coord differentes
									indexStationDep = index_station_grossier(nameDep) #Station precedente
									indexStationArr = index_station_grossier(nameArr) #Station courante

									if(indexStationDep != -1 and indexStationArr != -1): # On check que les stations existent et on les reupere
										depart = self.g.stations[indexStationDep] ###### 2
										arrivee = self.g.stations[indexStationArr] ###### 3
										tmp = Segment(line, depart, arrivee) #Pas d'horaire dans le cas a pied (calcule separement)
										tmp.setDistance()
										tmp.setDureeAPied() #L'objet est integre a ce stade
										print("| Walking correspondance created")	
										self.g.addSegment()						

							if(counter == 4): #Coord X cas funi et triviaux ON NE RENTRE PAS POUR LES CAS SANS COORDONNEES car counter jamais 4
								coordXDep = float(list_values_prec[counter])
								coordXArr = float(list_values[counter])
								counter += 1

							if(counter == 5): #Coord Y cas funi et triviaux
								coordYDep = float(list_values_prec[counter])
								coordYArr = float(list_values[counter])
								counter += 1

								#Derniere iteration on effectue l'affectation si possible
								indexStationDep = index_station_exact(nameArr, coordXDep, coordYDep) #Station precedente
								indexStationArr = index_station_exact(nameArr, coordXArr, coordYArr) #Station courante

								if(indexStationDep != -1 and indexStationArr != -1):
									depart = self.g.stations[indexStationDep] ###### 2
									arrivee = self.g.stations[indexStationArr] ###### 3
									
									if "funi" in line:
										tmp = Segment(line, depart, arrivee)
										tmp.setDistance()
										tmp.setDureeFuni() #Objet integre a ce stade
										print("|| Funicular segment created")

							if(counter == 6):
									tpsDep = list_values_prec[count]
									tpsArr = list_values[count]

									tmp = Segment(line, depart, arrivee)
									tmp.setDistance()
									tmp.setDureeMetro(tpsDep, tpsArr) #Objet integre a ce stade
									print("| Segment created")


							else:
								counter += 1



if __name__ == "__main__":

	s = Scanner()
	s.parseStations()
	s.g.allStationToString()
	












