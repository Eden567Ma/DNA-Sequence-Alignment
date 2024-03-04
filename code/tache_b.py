import sys
import os
sys.path.append('./')

import resource

import helpers as h

# tache B

# calcul DIST_1
def DIST_1(x: str, y: str):
    n = len(x) + 1
    m = len(y) + 1

    # initialise D de taille M x N
    D = [[0 for j in range(m)] for i in range(n)]

    # remplir la colonne de gauche avec le cout de del
    for i in range(0, n):
        D[i][0] = i * h.c_del

    # remplir la premiere ligne avec le cout de ins
    for j in range(0, m):
        D[0][j] = j * h.c_ins

    # pour chaque case a partir de la,
    for i in range(1, n):
        for j in range(1, m):
            # trouver quelle aurait ete l'operation la moins couteuse
            D[i][j] = min( D[i-1][j] + h.c_del,
                          D[i][j-1] + h.c_ins,
                          D[i-1][j-1] + h.c_sub(x[i-1], y[j-1]))

    return D#[len(x)][len(y)]

# calcul SOL_!
def SOL_1(x: str, y: str, T: list):
    # init
    u = []
    v = []
    i = len(x)
    j = len(y)

    # on commence au bout de x et y
    while i > 0 and j > 0:
        # si il faut inserer une lettre
        if T[i][j] == T[i][j-1] + h.c_ins:
            u.append( '-' )
            v.append( y[j-1] )
            j = j-1
        # si il faut retirer une lettre
        elif T[i][j] == T[i-1][j] + h.c_del:
            u.append( x[i-1] )
            v.append( '-' )
            i = i-1
        # si il faut substituer une lettre
        elif T[i][j] == T[i-1][j-1] + h.c_sub(x[i-1], y[j-1]):
            u.append( x[i-1] )
            v.append( x[i-1] )
            i = i-1
            j = j-1
        #print(f"i: {i}, j: {j}")

    # si il reste encore des lettres dans x
    while i > 0:
        u.append( x[i-1] )
        v.append( '-' )
        i = i-1

    # si il reste encore des lettres dans y
    while j > 0:
        u.append( '-' )
        v.append( y[j-1] )
        j = j-1

    # puisqu'on a append a la place de insert dans head,
    # on inverse l'ordre des resultats
    u.reverse()
    v.reverse()

    return u, v

def PROG_DYN(x: str, y: str):
    # d'abbord calculer le tableau entier
    D = DIST_1(x, y)
    s = SOL_1(x, y, D)
    print(f"Distance d'edition: {D[len(x)][len(y)]}")
    print(f"Alignement minimal: {s}")
    return s


#a, b = h.lire_fichier("Instances_genome/Inst_0000010_8.adn")

#print(a)
#print(b)
#d = DIST_1(a, b)
#print(d)
#print(SOL_1(a, b, d))

#PROG_DYN(a, b)


"""
fmesure = open("mesure_tache_b_mem.txt", "w")

beg = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

for filename in sorted(os.listdir(directory)):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        if f == "Instances_genome/Inst_0050000_6.adn":
            fmesure.close()
            exit(0)
        print(f)
        a, b = h.lire_fichier(f)
        #res = DIST_NAIF(a, b)
        temps = h.time_function(PROG_DYN, a, b)
        res = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - beg
        print(f"{res}")
        fmesure.write(f"{f.split('/')[1]},{res}\n")
        fmesure.flush()
"""
"""
fmesure = open("mesure_tache_b_dist_1.txt", "w")

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        if f == "Instances_genome/Inst_0050000_6.adn":
            fmesure.close()
            exit(0)
            #pass
        print(f)
        a, b = h.lire_fichier(f)
        #res = DIST_NAIF(a, b)
        temps = h.time_function(DIST_1, a, b)
        print(f"{temps}")
        fmesure.write(f"{f.split('/')[1]}\n{temps}\n")

"""
