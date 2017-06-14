# -*- coding: utf-8 -*- 

from graphe import *

import sys

class Parser:

    g = None

    def __init__(self):
        self.g=Graphe()

    def calculArrete(self):
        f = open("Paris_Metro2.txt",'r')
        lignes  = f.read().splitlines()
        f.close()
        name="tmp"
        nameDest="tmp"
        terminus=["tmp","tmp"]
        for ligne in lignes:
            if(ligne.strip() != ''): #ignore empty lines
                if "###" in ligne:
                    list_values = ligne.split(":")
                    terminus=list_values[1].split("--")
                    name=terminus[0]
                    print "##"
                else: 
                    list_values = ligne.split(":")
                    nameDest=list_values[1]
                    if(nameDest not in name):
                        
                        print "Arrete %s : %s" %(name,nameDest)
                    name=list_values[1]

    def parse(self):
        f = open("metro.txt",'r')
        lignes  = f.read().splitlines()
        f.close()
        counter = 0
        name_corr="tmp"
        for ligne in lignes:
            if(ligne.strip() != ''):
                if "###" in ligne:
                    line="tmp"
                    list_values = ligne.split(":")
                    counter=1
                    for item in list_values:
                        if(item!='\n'):
                            if(counter==1):
                                line=item
                                counter=counter+1
                            elif(counter==3 and ("corr" in line)):
                                name_corr=item
                                counter=counter+1
                            else:
                                counter=counter+1
                else: 
                    list_values = ligne.split(":")
                    counter=1
                    line="tmp"
                    sens="tmp"
                    name="tmp"
                    x=0
                    y=0
                    first=0
                    last=0
                    for item in list_values:
                        if(item!='\n'):
                            if(counter==1):
                                line=item  
                                counter=counter+1
                            elif(counter==2):
                                sens=item
                                counter=counter+1
                            elif(counter==3):
                                name=item
                                #On renvoie un tableau correspondant à toutes les stations qui ont le nom que l'on cherche 
                                #indépendamment du sens et de la ligne c'est pourquoi on ajoute les correspondances dans Station et non Arret
                                if(line=='corr' and name_corr!="tmp"):
                                    #Quand on trouve une correspondance qui est différente de l'intitulé on ajoute la station à l'intitulé
                                    #et l'intitulé à la station
                                    if(name not in name_corr):
                                        indexIntitule = self.g.index_station(name_corr)
                                        indexStation = self.g.index_station(name)
                                        for i in indexIntitule:
                                            for j in indexStation:
                                                self.g.stations[i].addCorrespondance(self.g.stations[j])
                                        print "Correspondance for %s added" %name_corr
                                        for i in indexStation:
                                            for j in indexIntitule:
                                                self.g.stations[i].addCorrespondance(self.g.stations[j])
                                        print "Correspondance for %s added" %name
                                        
                                counter=counter+1
                            elif(counter==4):
                                x=float(item)
                                counter=counter+1
                            elif(counter==5):
                                y=float(item)
                                if (line=='funi'):
                                    self.g.add_station(name,x,y)
                                    self.g.stations[-1].addArret(line,sens,"N/D","N/D")
                                counter=counter+1
                            elif(counter==6):
                                first=item
                                counter=counter+1
                            elif(counter==7):
                                last=item
                                #Clause de protection mais on ne devrait jamais entrer dedans
                                if(x==0 or y==0 or first==0 or last==0):
                                    print("")
                                else:    
                                    self.g.add_station(name, x, y)
                                    self.g.stations[-1].addArret(line,sens,first,last)
                                    counter=counter+1
                            """else:
                                counter=counter+1"""
                    #En sortant du counter=3, le programme fait counter+1 donc à la fin de la boucle quand on a lu 3 arguments,
                    #le programme en a compté 4 et respectivement 6 quand on a lu 5 arguments
                    if(counter==4 and first==0 and last==0):
                        if("corr" not in line):
                            #print "%s - %s - %d" %(line, name, counter)
                            self.g.add_station(name,0,0)
                            self.g.stations[-1].addArret(line,sens,"N/D","N/D")
                    elif(counter==6 and first==0 and last==0):
                        if("corr" not in line):
                            #print "%s - %s - %d" %(line, name, counter)
                            self.g.add_station(name,x,y)
                            self.g.stations[-1].addArret(line,sens,"N/D","N/D")
        self.g.toString()

if __name__ == '__main__':
    p=Parser()
    p.parse()
    p.calculArrete()


