from station import *
from segment import *

class Graphe:

    def __init__(self):
        self.stations = []    # creates a new empty list for each station
        self.arretes=[]

    def add_segment(self, depart, arrivee, distance, duree):
        a = Segment(depart, arrivee, distance, duree)
        self.arretes.append(a)

    def add_station(self, name, x, y):
        s = Station(name, x, y)
        self.stations.append(s)

    def index_station(self, name):
        index = []
        self.counter=0
        counter=0
        #print "Searching for %s" %name
        for station in self.stations:
            if (name == station.name):
                #print "Station found %s at %d:%d(searched %s)" %(station.name, station.coordX, station.coordY, name)
                index.append(counter)
            else:
                counter=counter+1
        return index

    def all_station(self):
        for station in self.stations:
            print "Station %s at %d.%d" %(station.name,station.coordX,station.coordY)

    def all_segment(self):
        for segment in self.arretes:
            segment.toString()

    def testIndex(self, i):
        for j in i : 
            print "Station %s at %d.%d" %(self.stations[j].name,self.stations[j].coordX,self.stations[j].coordY)


    def toString(self):
        print "##### GRAPHE #####"
        print " "
        print "@@@@@ STATION @@@@@"
        for station in self.stations:
            station.toString()
        print " "