from segment import *

class Station:

    def __init__(self, name, x, y):
        '''Constructeur d'une station et de ses segments associes'''
        self.name = name # Nom de la station
        self.coordX = x # (X)
        self.coordY = y # (Y)
        self.segmentsSuiv = [] #Segments suivants

    def addSuivant(self, line, sens, first, last, distance, duree):
        '''Ajoute un segment dont la station courante est le depart'''
        segToAdd = Segment(line, depart, arrivee, distance, duree)
        found = 0

        for segment in self.segmentsSuiv:
            if (segment.stationDepart == segToAdd.stationDepart and segment.stationArrivee == segToAdd.arrivee and segment.numLigne == segToAdd.numLigne):
                found = 1
                #print "%s>%s already added" %(segToAdd.depart, segToAdd.arrivee)
                break

        if(found == 0):
            self.arret.append(segToAdd)

    def toString(self):
        print("Station [%s] at (x = %d; y = %d)") %(self.name , self.coordX ,self.coordY)
        if(len(self.segmentsSuiv) != 0):
            print("Segments accessibles depuis [%s] :") %(self.name)
            for segments in self.segmentsSuiv:
                segments.toString() #Segment


if __name__ == "__main__":

    s1 = Station("La Defense", 77, 465)
    s1.toString()