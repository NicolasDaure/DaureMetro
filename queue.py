import collections

class Queue:

	def __init__(self):
		'''Cree une liste avec ajout rapide et methode de retrait a gauche et at droite'''
        self.elements = collections.deque() 


    def estVide(self):
    	'''Retourne vrai si la liste est vide'''
        return len(self.elements) == 0
    
    def addElem(self, x):
    	'''Ajotue un element a la liste'''
        self.elements.append(x)
    
    def get(self): 
    	'''Retourne l'element de la liste le plus a gauche'''
        return self.elements.popleft()