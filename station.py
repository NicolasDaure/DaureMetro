from segment import *

class Station:

    def __init__(self, name, x, y):
        '''Constructeur d'une station et de ses segments associes'''
        self.name = name # Nom de la station
        self.coordX = x # (X)
        self.coordY = y # (Y)
        self.segmentsSuiv = [] #Segments suivants
        self.aPiedSuiv = [] #Segments suivants à pied (à développer)


    def addSuivant(self, line, sens, first, last, distance, duree):
        '''Ajoute un segment dont la station courante est le départ'''
        segToAdd = Segment(line, depart, arrivee, distance, duree)
        found = 0

        for segment in self.segmentsSuiv:
            if (segment.stationDepart == segToAdd.stationDepart and segment.stationArrivee == segToAdd.arrivee and segment.numLigne == segToAdd.numLigne):
                found = 1
                #print "%s>%s already added" %(segToAdd.depart, segToAdd.arrivee)
                break

        if(found == 0):
            self.arret.append(segToAdd)


    def addAPiedSuivant(self, line, sens, first, last, distance, duree):
        '''Ajoute une correspondance à pied à la station (inutile pour le moment)'''
        segToAdd = Segment(line, depart, arrivee, distance, duree)
        found = 0

        for corr in self.aPiedSuiv:
            if (corr == c and c.name != self.name):
                found = 1
                #print "%s>%s already added" %(segToAdd.depart, segToAdd.arrivee)
                break

        if(found == 0):
            self.aPiedSuiv.append(segToAdd)


    def toString(self):
        print("Station [%s] at (x = %d; y = %d)") %(self.name , self.coordX ,self.coordY)
        print("Segments accessibles depuis [%s] :") %(self.name)
        for segments in self.segmentsSuiv:
            segments.toString() #Segment

        if(len(self.correspondance) != 0): #Affichage des correspondances accessibles en marchant
            print ("Correspondances of station : %s") %self.name
            for corr in self.aPiedSuiv:
                corr.toString() #Segment

        print ("")