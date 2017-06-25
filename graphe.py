from station import *
from segment import *
from binheap import *

class Graphe:

    def __init__(self):
        '''Constructeur du graphe soit un ensemble d'arretes et noeuds'''
        self.stations = [] #Liste des stations
        self.segments = []  #Liste des arretes

    def addSegment(line, depart, arrivee, distance, duree):
        '''Ajoute un segment'''
        segToAdd = Segment(line, depart, arrivee, distance, duree)
        found = 0
        for segment in self.segments:
            if (segment.stationDepart == segToAdd.stationDepart and segment.stationArrivee == segToAdd.stationArrivee and segment.numLigne == segToAdd.numLigne):
                found = 1
                #print "%s>%s already added" %(segToAdd.depart, segToAdd.arrivee)
                break

        if(found == 0):
             self.segments.append(segToAdd)

    def addStation(self, name, x, y): #Ajout à la liste des stations du graphe
        stationToAdd = Station(name, x, y)
        found = 0
        for station in self.stations:
            if (stationToAdd.name == station.):
                found = 1
                #print "Correspondance %s already added for %s" %(corr.name, c.name)
                break

        if(found == 0):
            self.stations.append(s)

    def index_station(self, name):
        index = []
        self.counter = 0
        counter = 0
        #print "Searching for %s" %name
        for station in self.stations:
            if (name == station.name):
                #print "Station found %s at %d:%d(searched %s)" %(station.name, station.coordX, station.coordY, name)
                index.append(counter)

            else:
                counter += 1

        return index

    def all_station(self):
        for station in self.stations:
            print ("Station %s at %d.%d" %(station.name,station.coordX,station.coordY))

    def all_segment(self):
        for segment in self.arretes:
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