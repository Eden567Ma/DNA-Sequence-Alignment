import sys
import math
import os
sys.path.append('./')

import helpers as h

# Tache A

def DIST_NAIF(x: str, y: str) -> float:
    return DIST_NAIF_REC(x, y, -1, -1, 0, math.inf)

def DIST_NAIF_REC(x: str, y: str, i: int, j: int, c: int, dist: int) -> float:
    #print(f"x: {x}\t\ty: {y}")
    #print(f"i: {i}  j: {j}")
    # ajuster longueur
    n = len(x) - 1
    m = len(y) - 1

    # si on a atteind la fin des mots
    if i == n and j == m:
        if c < dist:
            dist = c
    # sinon
    else:
        # si il reste encore des deux mots
        if i < n and j < m:
            dist = DIST_NAIF_REC(x, y, i+1, j+1, c+h.c_sub(x[i+1], y[j+1]), dist)
        # si il reste que de x
        if i < n:
            dist = DIST_NAIF_REC(x, y, i+1, j, c+h.c_del, dist)
        # si il reste que de y
        if j < m:
            dist = DIST_NAIF_REC(x, y, i, j+1, c+h.c_ins, dist)
    return dist

# tests DIST_NAIF

#tester(DIST_NAIF, "Instances_genome/Inst_0000010_44.adn", 10)
#tester(DIST_NAIF, "Instances_genome/Inst_0000010_7.adn", 8)
#tester(DIST_NAIF, "Instances_genome/Inst_0000010_8.adn", 2)


# enregistrer les mesures de DIST_NAIF
fmesure = open("mesure_tache_a.txt", "w")

for filename in os.listdir(h.directory):
    f = os.path.join(h.directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        a, b = h.lire_fichier(f)
        res = DIST_NAIF(a, b)
        temps = h.time_function(DIST_NAIF, a, b)
        print(f"{temps}")
        fmesure.write(f"{f.split('/')[1]}\n{temps}\n")


