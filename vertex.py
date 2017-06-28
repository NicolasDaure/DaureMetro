import sys

class Vertex:

	def __init__(self, station):
		self.id = station
		self.adjacents = {}
		self.distance = sys.maxint
		self.parcouru = False
		self.papa = None


	def add_Voisin(self, voisin, poids = 0):
		self.adjacents[voisin] = poids


	def get_Connexions(self):
		return self.adjacents.keys()

	def get_Id(self):
		return self.id

	def get_Poids(self, voisin):
		return self.adjacents[voisin]

	def get_Distance(self):
		return self.distance


	def set_Papa(self, geniteur):
		self.papa = geniteur

	def set_Parcouru(self):
		self.parcouru = True

	def set_Distance(self, dist):
		self.distance = dist