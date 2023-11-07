import numpy as np

from matriser import *
from verktøy import *


def endemoment(punkt, nelem, elem, L, r, EI, EA):
    endeM = np.empty((nelem, 6)) #Lager en tom liste

    for i in range(nelem):
        n1 = int(elem[i][0])
        n2 = int(elem[i][1])

        L_1 = L[(n1 * 3) : ((n1 * 3) + 3)]
        L_2 = L[(n2 * 3) : ((n2 * 3) + 3)]

        L_tot = np.zeros(6)

        for n in range(0, 2):
            L_tot[n] = L_1[n]

        for m in range(0, 2):
            L_tot[m + 2] = L_2[m]
            
        theta = vinkel(elem[i], punkt)
        T = transformasjonsmatrise(theta)

        L_tot = T*np.transpose(np.matrix(L_tot))

        temp_r = np.transpose(np.matrix(r[i]))
        k = np.matrix(lokal_matrise(EI[i], EA[i], L[i]))


        S = k*L_tot + temp_r

        endeM[i] = np.array(np.transpose(S))

    return endeM 
