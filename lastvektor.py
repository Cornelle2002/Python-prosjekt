import numpy as np

from verktøy import *
from matriser import *

def lastvektor(r, npunkt, punkt, nelem, elem):
    # Lager 1D-liste med 3 frihetsgrader * knutepunkter
    R = np.zeros(npunkt * 3)
    for i in range(nelem): # Itererer gjennom antall elementer
        theta = vinkel(elem[i], punkt) # Finner vinkel i globalt system

        temp_r = np.transpose(r[i]) @ np.transpose (transformasjonsmatrise(theta))
    
        k_1 = int(elem[i][0])
        k_2 = int(elem[i][1]) 

        for j in range(3):
            index = (3 * k_1) + j
            R[index] += temp_r[j]
            index = (3 * k_2) + j
            R[index] += temp_r[j + 3] 

    return R # Returnerer lastvektor med informasjon om hvert knutepunkt

def punktkrafeter(elem, npunkt, punkt, npunlast, punlast, elementlengder):
    R1 = np.zeros(npunkt*3)

    for i in range(npunlast):

        element = int(punlast[i][0])
        a = int(punlast[i][2])
        theta = int(vinkel(elem[element], punkt))
        l = int(elementlengder[element])
        start = int(elem[element][0])
        slutt = int(elem[element][1])

        
        if a == 0:
            n = (start) * 3 + 1
            R1[n] = int(punlast[i][1])
        elif a == l:
            n = (slutt) * 3 + 1
            R1[n] = int(punlast[i][1])

    return R1