import numpy as np


#Lager lokal stivhetmatrise 
def lokal_matrise(EI, EA, L):
    
    k = np.zeros((6, 6))

    k[0][0] = EA / L 
    k[0][1] = 0
    k[0][2] = 0
    k[0][3] = -EA / L
    k[0][4] = 0
    k[0][5] = 0

    k[1][0] = 0
    k[1][1] = 12 * EI / L ** 3
    k[1][2] = -6 * EI / L ** 2
    k[1][3] = 0
    k[1][4] = -12 * EI / L ** 3
    k[1][5] = -6 * EI / L ** 2

    k[2][0] = 0
    k[2][1] = -6 * EI / L ** 2
    k[2][2] = 4 * EI / L
    k[2][3] = 0
    k[2][4] = 6 * EI / L ** 2
    k[2][5] = 2 * EI / L

    k[3][0] = -EA / L
    k[3][1] = 0
    k[3][2] = 0
    k[3][3] = EA / L
    k[3][4] = 0
    k[3][5] = 0

    k[4][0] = 0
    k[4][1] = -12 * EI / L ** 3
    k[4][2] = 6 * EI / L ** 2
    k[4][3] = 0
    k[4][4] = 12 * EI / L ** 3
    k[4][5] = 6 * EI / L ** 2

    k[5][0] = 0
    k[5][1] = -6 * EI / L ** 2
    k[5][2] = 2 * EI / L
    k[5][3] = 0
    k[5][4] = 6 * EI / L ** 2
    k[5][5] = 4 * EI / L

    return k # returnerer lokal stivhetsmatrise


#Lager transformasjonsmatrisen
def transformasjonsmatrise(rad):
    T = np.zeros((6, 6))

    T[0][0] = np.cos(rad)
    T[0][1] = np.sin(rad) 
    T[0][2] = 0
    T[0][3] = 0
    T[0][4] = 0
    T[0][5] = 0

    T[1][0] = -np.sin(rad) 
    T[1][1] = np.cos(rad) 
    T[1][2] = 0
    T[1][3] = 0
    T[1][4] = 0
    T[1][5] = 0

    T[2][0] = 0
    T[2][1] = 0
    T[2][2] = 1
    T[2][3] = 0
    T[2][4] = 0
    T[2][5] = 0

    T[3][0] = 0
    T[3][1] = 0
    T[3][2] = 0
    T[3][3] = np.cos(rad) 
    T[3][4] = np.sin(rad) 
    T[3][5] = 0

    T[4][0] = 0
    T[4][1] = 0
    T[4][2] = 0
    T[4][3] = -np.sin(rad) 
    T[4][4] = np.cos(rad) 
    T[4][5] = 0

    T[5][0] = 0
    T[5][1] = 0
    T[5][2] = 0
    T[5][3] = 0
    T[5][4] = 0
    T[5][5] = 1

    return T
