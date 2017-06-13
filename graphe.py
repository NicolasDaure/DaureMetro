class Graphe:

    def __init__():
        self.stations = []    # creates a new empty list for each station
        self.arret = []    # creates a new empty list for each stop
        self.ligne = []    # creates a new empty list for each line

    def add_station(self, station):
        self.stations.append(station)

    def add_arret(self, stop):
        self.arret.append(stop)

    def add_ligne(self, line):
        self.ligne.append(line)