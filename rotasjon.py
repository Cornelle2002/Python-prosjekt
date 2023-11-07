import numpy as np

def rotasjoner(npunkt, L, skalering):

    rot = []                                            # Lager liste for rotasjons elementene
    
    for x in range(npunkt):                             # Itererer gjennom knutepunktene
        for y in range(3): 
            if y == 2:                                  # Henter ut hvert tredje elemetn fra L
                rot.append(L.item(x * 3 + y)*skalering) # Setter rotasjons elemnetet inn i listen
                
    return rot # Returnerer listen med rotasjons elementene