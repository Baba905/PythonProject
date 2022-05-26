import math
import random


def distance(p1,p2):
    dist_carre = (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2
    return  math.sqrt(dist_carre)


def recup_cordonne(namefile):

    tab = []
    tab1= []
    file = open(namefile, "r")
    for line in file:
        tab = line.split(' ')
        v = tab[0]
        x = float(tab[1])
        y = float(tab[2])
       #print(x,y)
        tab1.append([v,x,y])
    file.close()
    return  tab1

def calcul_chemin(list_ville):
    nbville= len(list_ville)
    first=list_ville[0]
    last=list_ville[nbville-1]
    totalChemin= distance(first,last)

    for i in range(nbville-1):
        totalChemin+=distance(list_ville[i],list_ville[i+1])

    return  totalChemin


def affiche_ville(listville):
    chemin=""
    for ville in listville:
        chemin+=(ville[0]+"->")
    chemin+=listville[0][0]
    print(chemin)

def tsp_naive(list_ville,n):
    i=0
    min_distance=calcul_chemin(list_ville)
    while i < n:
        random.shuffle(list_ville)
        actual_distance=calcul_chemin(list_ville)
        if min_distance> actual_distance:
            #print("ok",i)
            min_distance = actual_distance
        i+=1
    affiche_ville(list_ville)
    return  min_distance

def tsp_glouton(liste_ville, ville, chemin_court):
    if len(liste_ville)==0:
        return chemin_court
    else:
        prochain_ville = liste_ville[0]
        min = distance(ville,prochain_ville)
        for i in range(1,len(liste_ville)):
            if distance(ville,liste_ville[i])< min:
                prochain_ville = liste_ville[i]
                min = distance(ville,liste_ville[i])
        liste_ville.remove(prochain_ville)
        chemin_court.append(prochain_ville)
        return tsp_glouton(liste_ville,prochain_ville,chemin_court)





tsp= recup_cordonne('h:\Downloads\data.tsp\\16.tsp')

chemin_court= []
tsp_glouton(tsp, tsp[0], chemin_court)
affiche_ville(chemin_court)

print(calcul_chemin(chemin_court))