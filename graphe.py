from station import *
from ligne import *

class Graphe:

    def __init__(self):
        self.stations = []    # creates a new empty list for each station

    def add_station(self, name, x, y):
        s = Station(name, x, y)
        self.stations.append(s)

    def toString(self):
        print "##### GRAPHE #####"
        print " "
        print "@@@@@ STATION @@@@@"
        for station in self.stations:
            station.toString()
        print " "