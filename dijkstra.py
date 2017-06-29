from scan import *
import heapq


def cheminLePlusCourt(vertex, path):
	'''Fonction recursive reconstruisant le chemin depuis la destination a la source'''
	if vertex.papa:
		path.append(vertex.papa.get_Id())
		print ("")
		cheminLePlusCourt(vertex.papa, path)

	return

def dijkstra(graph, source, destination): #graphe, objet, objet

	source.set_Distance(0)

	queue_nonParcourus = [(v.get_Distance(),v) for v in graph]
	heapq.heapify(queue_nonParcourus)

	while len(queue_nonParcourus):
		queue_nP = heapq.heappop(queue_nonParcourus)
		courant = queue_nP[1]
		courant.set_Parcouru()

		for next in courant.adjacents:
			if next.parcouru:
				continue

			new_dist = courant.get_Distance() + courant.get_Poids(next)
			
			if new_dist < next.get_Distance():
				next.set_Distance(new_dist)
				next.set_Papa(courant)

		while len(queue_nonParcourus):
			heapq.heappop(queue_nonParcourus)

		queue_nonParcourus = [(v.get_Distance(),v) for v in graph if not v.parcouru]
		heapq.heapify(queue_nonParcourus)

if __name__ == '__main__':


	s = Scanner()

	####### GRAPHE TEST UNITAIRE #######

	# s1 = Station("a", 77, 465)
	# s2 = Station("b", 91, 461)
	# s3 = Station("c", 104, 457)
	# s4 = Station("d", 18, 453)

	# seg12 = Segment("1", s1, s2)
	# seg23 = Segment("1", s2, s3)
	# seg34 = Segment("1", s3, s4)
	# seg12.set_Distance()
	# seg23.set_Distance()
	# seg34.set_Distance()

	# s.g.stations.append(s1)
	# s.g.stations.append(s2)
	# s.g.stations.append(s3)
	# s.g.stations.append(s4)
	# s.g.segments.append(seg12)
	# s.g.segments.append(seg23)
	# s.g.segments.append(seg34)

	# s.g.allStationsToString()
	# s.g.allSegmentsToString()

	####### GRAPHE REEL ########

	s.parseStations()
	s.parseSegments()
	s.linkEponymStations() #Graphe pret pour la modelisation
	#s.g.allStationsToString()
	#s.g.allSegmentsToString()


	


	####### AFFICHAGE TEST DE LA STRUCTURE VERTEX ######

	# print "Graph data :"
	# for v in s.g:
	# 	for w in v.get_Connexions():
	# 		vid = v.get_Id().name
	# 		wid = w.get_Id().name
	# 		print"(%s, %s, %f)" %(vid, wid, v.get_Poids(w))
	
	s.build_Vertices("dist")

	source = s.g.get_Vertex(s.g.stations[0]) #Exemple a changer getClic1
	destination = s.g.get_Vertex(s.g.stations[15]) #Exemple a changer getClic2


	dijkstra(s.g, source, destination)
	path = [destination.get_Id()]
	cheminLePlusCourt(destination, path)

	for i in path:
		print (i.name)


	#######Interface graphique choix des stations et du mode



	





