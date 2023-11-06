import numpy as np

def rotasjoner(npunkt, L, skalering):

    rot = []
    
    #Henter ut hvert tredje element i b
    for x in range(npunkt):
        for y in range(3):
            if y == 2:
                rot.append(L.item(x * 3 + y)*skalering)
                
    return rot