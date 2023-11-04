import numpy as np

from verktøy import *

def lastvektor(fim, fis, npunkt, punkt, nelem, elem):
    # Lager 1D-liste med 3 frihetsgrader * knutepunkter
    R = np.zeros(npunkt * 3)
    for i in range(0, nelem): # Itererer gjennom antall elementer
        theta = vinkel(elem[i], punkt) # Finner vinkel i globalt system

        # Legger inn momentene
        R[int(elem[i][0]) * 3 + 2] += -fim[i][0]
        R[int(elem[i][1]) * 3 + 2] += -fim[i][1]

        # Dekomponerer Q til horisontal og vertikal komponent i globalt system 
        R[int(elem[i][0]) * 3 + 1] += -fis[i][0] * np.cos(theta)
        R[int(elem[i][1]) * 3 + 1] += -fis[i][1] * np.cos(theta)
        R[int(elem[i][0]) * 3] += -fis[i][0] * np.sin(theta)
        R[int(elem[i][1]) * 3] += -fis[i][1] * np.sin(theta)

    return R # Returnerer lastvektor med informasjon om hvert knutepunkt

def lastvektor_fiks(fim, fis, npunkt, punkt, nelem, elem):
    # Lager 1D-liste med 3 frihetsgrader * knutepunkter
    R = []
    for i in range(nelem):
        R.appen([0,0,0,0,0,0])
    for i in range(0, nelem): # Itererer gjennom antall elementer
        theta = vinkel(elem[i], punkt) # Finner vinkel i globalt system

        # Legger inn momentene
        R[int(elem[i][0]) * 3 + 2] += -fim[i][0]
        R[int(elem[i][1]) * 3 + 2] += -fim[i][1]

        # Dekomponerer Q til horisontal og vertikal komponent i globalt system 
        R[int(elem[i][0]) * 3 + 1] += -fis[i][0] * np.cos(theta)
        R[int(elem[i][1]) * 3 + 1] += -fis[i][1] * np.cos(theta)
        R[int(elem[i][0]) * 3] += -fis[i][0] * np.sin(theta)
        R[int(elem[i][1]) * 3] += -fis[i][1] * np.sin(theta)

    return R # Returnerer lastvektor med informasjon om hvert knutepunkt