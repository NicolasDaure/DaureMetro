from station import *
from arret import *
from ligne import *
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
        for item in list_values:
            if(item!='\n'):
                if(counter==3):
                    g.add_station(item)
                    counter=counter+1
                else:
                    #sys.stdout.write(item)
                    #sys.stdout.write(" ")
                    counter=counter+1
        #sys.stdout.write("\n")
    g.print_station()

if __name__ == '__main__':
    parse()


