from Tkinter import *
from math import *
import os

from dijkstra import *

# s = Scanner()
# s.parseStations()
# s.g.allStationsToString()
# s.parseSegments()
# s.g.allSegmentsToString()
# s.linkEponymStations()
# s.g.linkSegmentsToStations()
# s.g.allStationsToString()


############### Declarations ###############



s = Scanner()
s.parseStations()
s.parseSegments()
s.linkEponymStations()

fenetre=Tk()
fenetre.geometry("1400x900")
Fond=Canvas(fenetre,width=1000,height=1000,bg="white")
Fond.place(x=25,y=25)

t = 0
Lignes = []
SelecDep = 0
SelecArr = 0
AffM = 0

### Variables pour l'usilitation de fonction parcours
global SDep
SDep = None
global SArr
SArr = None
global path
path = None
global costOpti
costOpti = None
###


for segment in s.g.segments:
    if t == segment.numLigne:
        t=t
    else:
        Lignes.append(segment.numLigne)
        t=segment.numLigne
        
    
# seg=Segment()
# g=Graphe()
# s=Scanner()
# s.parseSegments
# s.g.allSegmentsToString()
# NLigne=[]

Couleur = ["#FFE436".lower(),"#21177D".lower(),"#708D23".lower(),"#708D23".lower(),"#AC1E44".lower(),"#ED7F10".lower(),"#87E990".lower(),"#FD6C9E".lower(),"#FD6C9E".lower(),"#D473D4".lower(),"#C7CF00".lower(),"#E79638".lower(),"#582900".lower(),"#00561B".lower(),"#80D0D0".lower(),"#800080".lower(),"black","#FF0000".lower(),"#6050DC".lower(),"#FFFF6B".lower(),"#FFFF6B".lower(),"#FFFF6B".lower(),"#16B84E".lower(),"pink","black"]

Width = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,5,5,5,5,5,5,5,4]


# for segment in s.g.segments:
#     Sd=segment.stationDepart
#     Sa=segment.stationArrivee
#     x=s.g.stations[s.g.stations.index(Sd)].coordX
#     print(x)

############### Fonctions ###############   

def distance(Xc,Yc,x,y):
    return sqrt((x-Xc)**2+(y-Yc)**2)

def motion(event):
    x, y = event.x, event.y
    d=[]
    i=0
    for station in s.g.stations:
        d.append(distance(x,y,Lx[i],Ly[i]))
        i+=1
    Dstat=min(d)
    Stat=d.index(Dstat)
    
    if Dstat<8:
        label.configure(text=s.g.stations[Stat].name)
        label.pack()
        label.place(x=(35+x),y=y+15)
        # print('{}, {}'.format(x, y))
    else:
        label.configure(text="",bg="white")
        fenetre.after(1)

def pointeur(event):
    x, y = event.x, event.y
    d=[]
    i=0
    
    global AffM
    global SelecDep
    global SelecArr
    for station in s.g.stations:
        d.append(distance(x,y,Lx[i],Ly[i]))
        Add.append(station)
        i+=1
    Dstat=min(d)
    Stat=d.index(Dstat)
    # print(Add[Stat])
    if Dstat<8:
        if SelecDep==0:
            TextDep.configure(text="Station de depart : ")
            TextDep.pack()
            TextDep.place(x=1100,y=65)
            # Dep=s.g.stations[Stat].name
            StatDepart.configure(text=s.g.stations[Stat].name,relief="ridge")
            StatDepart.pack()
            StatDepart.place(x=1100,y=100)
            SelecDep=Fond.create_oval(Lx[Stat]-8,Ly[Stat]+8,Lx[Stat]+8,Ly[Stat]-8,outline="#C8C8C8",width=4)
            global SDep
            SDep=Add[Stat]
            #print(SDep,SArr)
        elif SelecArr==0:
            TextArr.configure(text="Station de d'arrivee : ")
            TextArr.pack()
            TextArr.place(x=1100,y=650)
            # Arr=s.g.stations[Stat].name
            StatArrivee.configure(text=s.g.stations[Stat].name,relief="ridge")
            StatArrivee.pack()
            StatArrivee.place(x=1100,y=685)
            SelecArr=Fond.create_oval(Lx[Stat]-8,Ly[Stat]+8,Lx[Stat]+8,Ly[Stat]-8,outline="#C8C8C8",width=4)
            # print(Fond.coords(Selec[0])[0])
            AfficheMeth()
            global SArr
            SArr=Add[Stat]
            #print(SDep.name,SArr.name)
        else:
            TextArr.configure(text="Station de d'arrivee : ")
            StatArrivee.configure(text=s.g.stations[Stat].name)
            Fond.delete(SelecArr)
            SelecArr=Fond.create_oval(Lx[Stat]-8,Ly[Stat]+8,Lx[Stat]+8,Ly[Stat]-8,outline="#C8C8C8",width=4)
            global SArr
            SArr=Add[Stat]
            #print(SDep,SArr)



# def AffTpsReel():
#     global SDep
#     global SArr
#     print(SDep,SArr)

def RemoveBut():
    global SelecDep
    Fond.delete(SelecDep)
    SelecDep=0
    TextDep.configure(text="")
    StatDepart.configure(text="Selectionnez une Station")

def AfficheStat(event):
    x, y = event.x, event.y
    d=[]
    for i in range(390):
        d.append(distance(x,y,Lx[i],Ly[i]))
    Dstat=min(d)
    Stat=d.index(Dstat)
    
    if Dstat<8:
        TextDep.configure(text="Station de depart : ")
        TextDep.pack()
        TextDep.place(x=1150,y=65)
        StatDepart.configure(text=s.g.stations[Stat].name)
        StatDepart.pack()
        StatDepart.place(x=1175,y=100)
        # print('{}, {}'.format(x, y))

def AfficheMeth():
    TypeCal.configure(text="Choississez ce que vous voulez minimiser :")
    
    TypeCal.pack()
    Dist.pack()
    Tps.pack()
    
    TypeCal.place(x=1075,y=765)
    Dist.place(x=1100,y=800)
    Tps.place(x=1250,y=800)

def SupprMeth():
    TypeCal.configure(text="")
    Dist.place(x=1600,y=800)
    Tps.place(x=1600,y=800)

def Reini(event):
    global SelecDep
    global SelecArr
    SupprMeth()
    if SelecDep!=0:
        Fond.delete(SelecDep)

        TextDep.configure(text="")
        StatDepart.configure(text="Selectionnez une Station")
        if SelecArr!=0:
            TextArr.configure(text="")
            StatArrivee.configure(text="Selectionnez une Station")
            Fond.delete(SelecArr)
    elif SelecArr!=0:
        Fond.delete(SelecDep)
        TextArr.configure(text="")
        StatArrivee.configure(text="Selectionnez une Station")
    SelecDep=0
    SelecArr=0

def createDistanceTrip():
    
    global SDep, SArr, path, costOpti
    
    s.build_Vertices("dist") # Construction d'un graphe de parcours avec des poids de distance
    
    source = s.g.get_Vertex(SDep) #Exemple a changer getClic1
    destination = s.g.get_Vertex(SArr) #Exemple a changer getClic2
    
    dijkstra(s.g, source, destination)
    costOpti = destination.get_Distance()

    
    path = [destination.get_Id()]
    cheminLePlusCourt(destination, path)
    
    for i in path:
        print (i.name)

    
def createDurationTrip():
    
    global SDep, SArr, path, costOpti
    
    s.build_Vertices("time") # Construction d'un graphe de parcours avec des poids de duree

    source = s.g.get_Vertex(SDep) #Exemple a changer getClic1
    destination = s.g.get_Vertex(SArr) #Exemple a changer getClic2
    
    dijkstra(s.g, source, destination)
    costOpti = math.floor(destination.get_Distance() / 60)

    path = [destination.get_Id()]
    cheminLePlusCourt(destination, path)
    
    for i in path:
        print (i.name)
    

    


############# Corps #################

for i in range(len(Lignes)-1):
    for segment in s.g.segments:
        Sd=segment.stationDepart
        Sa=segment.stationArrivee
        # print(s.g.stations.index(Sd))
        Xd=1.5*s.g.stations[s.g.stations.index(Sd)].coordX
        Yd=1.5*s.g.stations[s.g.stations.index(Sd)].coordY
        Xa=1.5*s.g.stations[s.g.stations.index(Sa)].coordX
        Ya=1.5*s.g.stations[s.g.stations.index(Sa)].coordY
        if segment.numLigne==Lignes[i]:
            Fond.create_line(Xd,1050-Yd,Xa,1050-Ya,fill=Couleur[i],width=Width[i])           

for segment in s.g.segments:
    Sd=segment.stationDepart
    Sa=segment.stationArrivee
    # print(s.g.stations.index(Sd))
    Xd=1.5*s.g.stations[s.g.stations.index(Sd)].coordX
    Yd=1.5*s.g.stations[s.g.stations.index(Sd)].coordY
    Xa=1.5*s.g.stations[s.g.stations.index(Sa)].coordX
    Ya=1.5*s.g.stations[s.g.stations.index(Sa)].coordY
    if segment.numLigne==Lignes[24]:
        Fond.create_line(Xd,1050-Yd,Xa,1050-Ya,fill=Couleur[24],width=Width[24],dash=(10,3))


i=0
Lx=[]
Ly=[]
label=Label(fenetre, text="")
TextDep=Label(fenetre, text="")
StatDepart=Button(fenetre, text="",command=RemoveBut)
TextArr=Label(fenetre, text="")
StatArrivee=Button(fenetre, text="")
TypeCal=Label(fenetre, text="Choississez ce que vous voulez minimiser :")
Dist=Button(fenetre, text="Distance",width=11,height=2)#,command=createDistanceTrip)
Tps=Button(fenetre, text="Temps",width=11,height=2)#,command=createDurationTrip)
Add=[]
d=[]

for station in s.g.stations:
    # print(s.g.stations.index(Sd))
    X=1.5*s.g.stations[i].coordX
    Lx.append(X)
    Y=1.5*s.g.stations[i].coordY
    Ly.append(1050-Y)
    Fond.create_oval(Lx[i]-5,Ly[i]-5,Lx[i]+5,Ly[i]+5,fill="white",width=2)
    i+=1



        
fenetre.bind("<Button-1>", pointeur)
# fenetre.bind("<Button-1>", AfficheStat)
fenetre.bind("<Button-3>", Reini)
fenetre.bind('<Motion>', motion)

fenetre.mainloop()