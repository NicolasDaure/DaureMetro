from station import *
from segment import *
from binheap import *

class Graphe:

    def __init__(self):
        '''Constructeur du graphe soit un ensemble d'arretes et noeuds'''
        self.stations = [] #Liste des stations
        self.segments = []  #Liste des arretes

    def addSegment(line, depart, arrivee, distance, duree):
        '''Ajoute un segment à la liste de segments'''
        segToAdd = Segment(line, depart, arrivee, distance, duree)
        found = 0
        for segment in self.segments:
            if (segment.stationDepart == segToAdd.stationDepart and segment.stationArrivee == segToAdd.stationArrivee and segment.numLigne == segToAdd.numLigne):
                found = 1
                #print "%s>%s already added" %(segToAdd.depart, segToAdd.arrivee)
                break

        if(found == 0):
             self.segments.append(segToAdd)

    def addStation(self, name, x, y):
        '''Ajoute une station à la liste de stations'''
        stationToAdd = Station(name, x, y)
        found = 0
        for station in self.stations:
            if (station.name == stationToAdd.name and station.coordX == stationToAdd.coordX and station.coordY == stationToAdd.coordY):
                found = 1
                #print "Correspondance %s already added for %s" %(corr.name, c.name)
                break

        if(found == 0):
            self.stations.append(stationToAdd)

    def index_station(self, name, X, Y):
        '''Retourne l'index de la station dont on a les paramètres'''
        counter = 0
        found = False #Pour ne pas tout parcourir si la station est trouvée
        #print "Searching for %s" %name
        while found == False and  counter < len(self.stations):
            if (station.name == name and station.coordX == X and station.coordY = Y and found == 0):
                #print "Station found %s at %d:%d(searched %s)" %(station.name, station.coordX, station.coordY, name)
                found = True

            else:
                counter += 1

        return counter

    def allStationToString(self):
        for station in self.stations:
            print ("Station [%s] at (%d;%d)" %(station.name,station.coordX,station.coordY))

    def allSegmentToString(self):
        for segment in self.segments:
            segment.toString()

    def testIndex(self, i):
        for j in i : 
            print ("Station %s at %d.%d" %(self.stations[j].name,self.stations[j].coordX,self.stations[j].coordY))

    def toString(self):
        print ("########## GRAPHE ##########")
        print ("")
        print ("@@@@@ STATIONS @@@@@")

        for station in self.stations:
            station.toString()

        print ("----- ARRETES ------")

        for arrete in self.arretes:
            arrete.toString()

        print ("")