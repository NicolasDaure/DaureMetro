from graphe import *

import sys

def parse():
    g = Graphe()
    f = open("metro.txt",'r')
    lignes  = f.read().splitlines()
    f.close()
    counter = 0
    
    for ligne in lignes:
        list_values = ligne.split(":")
        counter=1
        ligne="tmp"
        sens="tmp"
        name="tmp"
        x=0
        y=0
        first=0
        last=0
        for item in list_values:
            if(item!='\n'):
                if(counter==1):
                    ligne=item
                    counter=counter+1
                elif(counter==2):
                    sens=item
                    counter=counter+1
                elif(counter==3):
                    name=item
                    counter=counter+1
                elif(counter==4):
                    x=float(item)
                    counter=counter+1
                elif(counter==5):
                    y=float(item)
                    counter=counter+1
                elif(counter==6):
                    first=item
                    counter=counter+1
                elif(counter==7):
                    last=item
                    if(x==0 or y==0 or first==0 or last ==0):
                        print("")
                    else:    
                        g.add_station(name, x, y)
                        g.stations[-1].addArret(ligne,sens,first,last)
                        counter=counter+1
                else:
                    counter=counter+1
    g.toString()

if __name__ == '__main__':
    parse()


