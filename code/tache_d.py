import sys
import os
sys.path.append('./')

import helpers as h

# tache D

# creer un tableau avec le mot vide de longueur k
def mot_gaps(k: int):
    return ['-'] * k

# aligne x (de longueur 1) avec y
def align_lettre_mot(x: str, y: str):
    n = len(x)
    m = len(y)

    assert n == 1

    # essayer de retrouver x
    for i in range(m):
        if x[0] == y[i]:
            return mot_gaps(i) + x + mot_gaps(m-(i+1))

    # si on ne trouve pas
    for i in range(m):
        if h.c_sub(x[0], y[i]) == 3:
            return mot_gaps(i) + x + mot_gaps(m-(i+1))

    return mot_gaps(m-1) + x # + mot_gaps(m-(i+1))


def coupure(x: str, y: str):
    n = len(x) + 1
    m = len(y) + 1

    # creer deux tableaux de 2 x M
    T = [[0 for j in range(m)] for i in range(2)] #distances
    I = [[0 for j in range(m)] for i in range(2)] #indexe

    # trouver ou couper
    c = len(x) // 2

    i = 1
    i2 = 1

    # remplir la premiere ligne
    for j in range(1, m):
        T[0][j] = j * h.c_del

    T[i][0] = 2

    # remplir la premiere colonne
    for j in range(m):
        I[0][j] = j
        I[1][j] = j

    # tout qu'on a pas atteint n
    while i < n:
        # ajuster i pour le tableau en modulo
        imod = (i) % 2
        ioff = (i-1) % 2

        # ajuster i2 pour le tableau en modulo
        i2mod = i2 % 2
        i2off = (i2-1) % 2

        for j in range(1, m):
            # calculer le cout de faire chaque modification
            cout_del = T[ioff][j] + h.c_del
            cout_ins = T[imod][j-1] + h.c_ins
            cout_sub = T[ioff][j-1] + h.c_sub(x[i-1], y[j-1])

            # retrouver le plus petit
            T[imod][j] = min( cout_del,
                            cout_ins,
                            cout_sub)

            # si on est deja cense couper
            if i > c:
                # si on a choisi de delete
                if T[imod][j] == cout_del:
                    I[i2mod][j] = I[i2off][j]

                # si on a choisi de inserer
                elif T[imod][j] == cout_ins:
                    I[i2mod][j] = I[i2mod][j-1]

                # si on a choisi de substituer
                elif T[imod][j] == cout_sub:
                    I[i2mod][j] = I[i2off][j-1]

        # si on en est a plus du point de coupure
        if T[ioff][j-1] + h.c_sub(x[i-1], y[j-1]) > c:
            #print("hit i2")
            i2 += 1

        # remplir la prochaine premiere case de la ligne oppose
        T[imod][0] = T[ioff][0] + h.c_del
        i += 1

        #print(f"imod {imod}\ti2md {i2mod}\tj {j}\t{I}")
    #print(I[i % 2])
    resultat = I[(len(x)-c-1) % 2][len(y)]
    return resultat

a, b = h.lire_fichier("Instances_genome/Inst_0000010_44.adn")
#print(coupure(a, b))

a, b = h.lire_fichier("Instances_genome/Inst_0000010_7.adn")
#print(coupure(a, b))

a, b = h.lire_fichier("Instances_genome/Inst_0000010_8.adn")
#print(coupure(a, b))

def SOL_2(x: str, y: str, u: str, v: str):
    n = len(x)
    m = len(y)

    # trouver la moitie
    i = n // 2

    # si y est un mot vide
    if n > 0 and m == 0:
        u.append( x )
        v.append( mot_gaps(n) )

    # si x est un mot vide
    elif n == 0 and m > 0:
        u.append( mot_gaps(m) )
        v.append( y )

    # si x est une lettre
    elif n == 1 and m > 0:
        u.append( align_lettre_mot(x,y) )
        v.append( y )

    # sinon, trouner diviser a j pour continuer
    elif n > 1 and m > 0:
        j = coupure(x, y)
        SOL_2(x[:i], y[:j], u, v)
        SOL_2(x[i:], y[j:], u, v)

    # retourner les solutions minimales
    return u, v

#u = []
#v = []

#a, b = h.lire_fichier("Instances_genome/Inst_0000010_7.adn")

#u, v = SOL_2(a, b, u, v)

#print(u)
#print(v)

"""h.tester(coupure, "Instances_genome/Inst_0000010_44.adn", 10)
h.tester(coupure, "Instances_genome/Inst_0000010_7.adn", 8)
h.tester(coupure, "Instances_genome/Inst_0000010_8.adn", 2)
"""


#a = list("ATTGTA")
#b = list("ATCTTA")
#print(SOL_2(a, b))

# mesurer D

directory = 'Instances_genome/'

fmesure = open("mesure_tache_d.txt", "w")

for filename in sorted(os.listdir(directory)):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        a, b = h.lire_fichier(f)
        u = []
        v = []
        #res = DIST_NAIF(a, b)
        temps = h.time_function(SOL_2, a, b, u, v)
        print(f"{temps}")
        fmesure.write(f"{f.split('/')[1]},{temps}\n")
        fmesure.flush()



#print(align_lettre_mot(["C"], ["T", "A", "G", "G"]))
