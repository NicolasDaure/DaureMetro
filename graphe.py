from station import *
from ligne import *

class Graphe:

    def __init__(self):
        self.stations = []    # creates a new empty list for each station

    def add_station(self, name, x, y):
        s = Station(name, x, y)
        self.stations.append(s)

    def index_station(self, name):
        index = []
        self.counter=0
        counter=0
        #print "Searching for %s" %name
        for station in self.stations:
            if (station.name in name):
                index.append(counter)
            else:
                counter=counter+1
        return index


    def toString(self):
        print "##### GRAPHE #####"
        print " "
        print "@@@@@ STATION @@@@@"
        for station in self.stations:
            station.toString()
        print " "