import time

directory = 'Instances_genome/'

# compare le resultat de la fonction avec ce qui est attendu
def tester(fun, filename: str, expected: int):
    a, b = lire_fichier(filename)
    res = fun(a, b)
    assert res == expected, f"Test {filename} a echoue, {expected} != {res}"


def lire_fichier(filename: str) -> (str, str):
    # ouvre un fichier f et extrait les lettres des mots
    with open(filename, 'r') as f:
        lines = f.readlines()
        a = list(lines[2].replace(" ", "").replace("\n", ""))
        b = list(lines[3].replace(" ", "").replace("\n", ""))
        #print(f"\"{a}\"")
        #print(f"\"{b}\"")
        f.close()
        return a, b

# notre alphabet
alphabet = ['A', 'T', 'C', 'G']

# complement de la lettre
def compl(a: str) -> str:
    if a == 'A':
        return 'T'
    if a == 'T':
        return 'A'
    if a == 'C':
        return 'G'
    if a == 'G':
        return 'C'

# on defini le cout pour ce projet
c_del = 2
c_ins = 2

def c_sub(a, b):
    if a == b:
        return 0
    elif compl(a) == b:
        return 3
    else:
        return 4

def time_function(fun, *args):
    start = time.process_time()
    fun(*args)
    end = time.process_time()
    return end - start
