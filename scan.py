# -*- coding: utf-8 -*-

from graphe import *
import sys

class Scanner:

	def __init__(self):
		self.g = Graphe()


	def parseStations(self):
		'''Création des noeuds du graphe avec coordonnées'''
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
						if (item != '\n'):
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
									self.g.addStation(name, coordX, coordY)

							else:
								counter += 1

	def parseSegments(self):
		f = open("metro.txt",'r')
		lignes = f.read().splitlines()
		f.close()

		counter = 0

		for ligne in lignes:

			if(ligne.strip() != ''):

				if "###" not in ligne: 

					list_values = ligne.split(":")

					counter = 1
					line, depart, arrivee, distance, duree = None, None, None, None, None






