%
import os

filename = "mesure_tache_d.txt"
#filename = "longueurs.txt"

f = open(filename, "r")
g = open(filename+"3", "w")
lines = f.readlines()



v = dict()
n = dict()

for line in lines:
    itera = str(line.split(",")[0].split("_")[1])
    if itera not in v:
        v[itera] = float(line.split(",")[1])
        n[itera] = 1
    if itera in v:
        v[itera] += float(line.split(",")[1])
        n[itera] += 1

    #vals = [float(k.split(",")[1]) for k in lines[line:line+3]]

for k, val in v.items():
    newline = str(int(k)) + "," + str(val / int(n[k])) + "\n"
    print(newline)
    g.write(newline)
    #n[k]


f.close()
g.close()
#print(l)


