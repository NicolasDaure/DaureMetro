from scan import *
import heapq


def cheminLePlusCourt(vertex, path):
	'''Fonction recursive reconstruisant le chemin depuis la destination a la source'''
	if vertex.papa:
		path.append(vertext.papa.get_Id())
		cheminLePlusCourt(vertex.papa, path)

	return

def dijkstra(graphe, source, destination):
	'''Effectue un parcours selon l'algorithme de Dijkstra sur le graphe qui est ainsi modifie et pret a etre lu'''

	source.set_Distance(0)

	queue_nonParcourus = [(v.get_Distance(),v) for v in graphe]
	heapq.heapify(queue_nonParcourus)

	while len(queue_nonParcourus):
		q_nP = heapq.heappop(queue_nonParcourus)
		courant  =q_nP[1]
		courant.set_Parcouru()

		for next in courant.adjacents:
			if next.parcouru:
				continue

			new_dist = courant.get_Distance() + courant.get_Poids(next)

			if new_dist < next.get_Distance():
				next.set_Distance(new_dist)
				next.set_Papa(courant)
				print ("Updated")

			else:
				print("Not updated")

		while len(queue_nonParcouru):
			heapq.heappop(queue_nonParcouru)

		queue_nonParcouru = [(v.get_Distance(),v) for v in graphe if not v.parcouru]
		heapq.heapify(queue_nonParcouru)




if __name__ == '__main__':

	s = Scanner()
	s.parseStations()
	#s.g.allStationsToString()
	s.parseSegments()
	s.linkEponymStations() #Graphe pret pour la modelisation
	#s.g.allSegmentsToString()

	s.build_Vertices() #Graphe pret pour les algorithmes

	source = s.g.get_Vertex(s.g.stations[0]) #Exemple a changer
	destination = s.g.get_Vertex(s.g.stations[3]) #Exemple a changer
	dijkstra(s.g, source, destination)

	path = [destination.get_Id()]
	cheminLePlusCourt(destination, path)

	for i in path:
		print i.name




