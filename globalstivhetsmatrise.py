import numpy as np

from EIEA import *
from verktøy import *
from matriser import *

def globalStivhetsmatrise(npunkt, punkt, nelem, elem, geo): 
    K =  np.zeros((3 * npunkt, 3 * npunkt)) 

    EI = ei(nelem, elem, geo)
    EA = ea(nelem, elem, geo)
    L = lengder(punkt, elem, nelem)
    
    for n in range(nelem):

        glob_frihet = []

        n1 = int(elem[n][0])
        n2 = int(elem[n][1])

        for j in range(3):
            glob_frihet.append(3*(n1) + (j))
        
        for j in range(3):
            glob_frihet.append(3*(n2) + (j))

        k = lokal_matrise(EI[n], EA[n], L[n])
        theta = vinkel(elem[n], punkt)
        T = transformasjonsmatrise(theta)
        k_g = np.transpose(T) @ k @ T

        for m in range(len(k_g)):
                for o in range(len(k_g)):
                    K[glob_frihet[m]][glob_frihet[o]] += k_g.item(m,o)

    return K # Returnerer global stivhetsmatrise 
