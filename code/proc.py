
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

"""
directory = 'Instances_genome/'

fmesure = open("a.txt", "w")

for filename in sorted(os.listdir(directory)):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        fi = open(f, "r")
        a = fi.readlines()[0]

        #res = DIST_NAIF(a, b)
        #temps = h.time_function(PROG_DYN, a, b)
        #print(f"{temps}")
        fmesure.write(f"{f.split('/')[1]},{a}")
        fmesure.flush()
        fi.close()
"""
