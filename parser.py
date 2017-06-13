import sys

def parse():
    g = Graphe()
    f = open("metro.txt",'r')
    lignes  = f.read().splitlines()
    f.close()
    
    for ligne in lignes:
        list_values = ligne.split(":")
        for item in list_values:
            if(item!='\n'):
                sys.stdout.write(item)
                sys.stdout.write(" ")
        sys.stdout.write("\n")

if __name__ == '__main__':
    parse()

