import numpy as np

from EIEA import *
from verktøy import *
from matriser import *

def globalStivhetsmatrise(npunkt, punkt, nelem, elem, geo): 

    K = np.zeros((3 * npunkt, 3 * npunkt)) # Oppretter 2D-vektor 30x30
    EI = ei(nelem, elem, geo) # Finner EI-liste
    EA = ea(nelem, elem, geo) # Finner EA-liste
    L = lengder(punkt, elem, nelem) # Finner elementlengde-liste

    for i in range(nelem): # Ittererer gjennom elementene
        k = lokal_matrise(EI[i], EA[i], L[i]) # Oppretter lokalstivhetsmatrise for hvert element
        vinkel_rad = vinkel(elem[i], punkt)
        T = transformasjonsmatrise(vinkel_rad)
        T_Transponert = np.linalg.inv(T)
        k_g = T @ k @ T_Transponert
        n1j = int(elem[i][0])
        n2j = int(elem[i][1])

        for rad in range(0, 3):
            for col in range(0, 3):
                K[n1j * 3 + rad][n1j * 3 + col] += k_g[rad][col]
                K[n1j * 3 + rad][n2j * 3 + col] += k_g[rad][col + 3]
                K[n2j * 3 + rad][n2j * 3 + col] += k_g[rad + 3][col + 3]
                K[n2j * 3 + rad][n1j * 3 + col] += k_g[rad + 3][col]

    return K # Returnerer global stivhetsmatrise 
