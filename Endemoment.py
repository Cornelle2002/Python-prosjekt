import numpy as np

from matriser import *
from verktøy import *

def spennings(punkt, nelem, elem, elementlengder, rot, fim, fis, EI, EA): 
    spenningsresultanter = np.zeros((nelem, 6)) # Lager 2D-liste

    for i in range(nelem):
        ende1 = int(elem[i][0])
        ende2 = int(elem[i][1])
        r = np.zeros(6) # Setter opp vektor med deformasjoner
        for j in range(3):
            r[j] = rot[ende1 * 3 + j]
            r[j + 3] = rot[ende2 * 3 + j]

        # Transformerer r så vi får lokale deformasjoner
        theta = vinkel(elem[i], punkt)
        T = transformasjonsmatrise(theta)
        V = np.matmul(np.transpose(T), r)
        S_f = np.zeros(6) # Setter opp vektor med fastinnspenningskrefter [aksial, skjær, moment]

        for n in range(0, 2):
            S_f[n * 3] = 0
            S_f[n * 3 + 1] = fis[i][n]
            S_f[n * 3 + 2] = fim[i][n]

        # Lokal stivhetsmatrise
        k = lokal_matrise(EI[i], EA[i], elementlengder[i])

        # Spenningsresultant til element
        kV = np.matmul(k, V)
        S = np.zeros(6)

        for m in range(6):
            S[m] = kV[m] + S_f[m]

        spenningsresultanter[i] = S

    return spenningsresultanter



def midtM(spenningsresultanter, nlast, last, npunktlast, punktlast, nelem, elementlengder):
    midtMom = np.zeros(nelem)  # Initialize 1D array

    for i in range(nelem):
        M1 = -spenningsresultanter[i][2]
        M2 = -spenningsresultanter[i][5]
        midtMom[i] = (M1 + M2) / 2

    # Add contributions from distributed loads
    for i in range(nlast):
        nr = int(last[i][0])
        L = elementlengder[nr]
        q1 = last[i][1]
        q2 = last[i][2]

        midtMom[nr] += q1 * (L / 2) / (6 * L) * (2 * L ** 2 - 3 * L * L / 2 + (L / 2) ** 2)
        midtMom[nr] += q2 * (L / 2) / (6 * L) * (2 * L ** 2 - 3 * L * L / 2 + (L / 2) ** 2)

    # Add contributions from point loads
    for i in range(npunktlast):
        id = int(punktlast[i][0])
        P = punktlast[i][1]
        a = punktlast[i][2]
        L = elementlengder[id]

        if a == L / 2:
            midtMom[id] += P * L / 4

    return midtMom 
