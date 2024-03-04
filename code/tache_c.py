import sys
import os
sys.path.append('./')

import helpers as h

# Tache C

def DIST_2(x: str, y: str):
    n = len(x) + 1
    m = len(y) + 1

    # on initialise D avec que 2 rangees
    D = [[0 for j in range(m)] for i in range(2)]

    # remplir la colonne
    for i in range(0, 2):
        D[i][0] = i * h.c_del

    # remplir la ligne
    for j in range(0, m):
        D[1][j] = j * h.c_ins
            #print(f"i: {i}, j: {j}")

    # parcourir de de 1 a n
    for i in range(1, n):
        # on calcule quel est la reele ligne et son complement
        imod = (i) % 2
        ioff = (i-1) % 2

        # remplir la premiere case avec ce qui aurait du etre la dans D
        D[ioff][0] = D[imod][0] + h.c_del

        for j in range(1, m):
            # refaire la meme chose qu'en DIST_1 mais subustituant i pour imod et i-1 pour ioff
            D[ioff][j] = min( D[imod][j] + h.c_del,
                          D[ioff][j-1] + h.c_ins,
                          D[imod][j-1] + h.c_sub(x[i-1], y[j-1]))


    # retourner la derniere case de la ligne
    return D[len(x) % 2][len(y)]


def PROG_DYN(x: str, y: str):
    D = DIST_2(a, b)
    #s = SOL_1(a, b, D)
    print(f"Distance d'edition: {D}")
    #print(f"Alignement minimal: {s}")


#a, b = h.lire_fichier("Instances_genome/Inst_0000010_44.adn")

#D = DIST_2(a, b)

#print(D)
#print(SOL_1(a, b, d))

#PROG_DYN(a, b)

# mesurer la memoire de c

fmesure = open("mesure_tache_c_mem.txt", "w")

for filename in sorted(os.listdir(h.directory)):
    f = os.path.join(h.directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        a, b = h.lire_fichier(f)
        #res = DIST_NAIF(a, b)
        temps = h.time_function(PROG_DYN, a, b)
        print(f"{temps}")
        fmesure.write(f"{f.split('/')[1]}\n{temps}\n")
        fmesure.flush()

