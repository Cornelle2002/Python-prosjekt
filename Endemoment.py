import numpy as np

from matriser import *
from verktøy import *

def spenningsRes(punkt, nelem, elem, elementlengder, rot, fim, fis, EI, EA): 
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
    midtMom = np.zeros(nelem) # Lager 1D-liste

    for i in range(nelem): 
        M1 = -spenningsresultanter[i][2]
        M2 = -spenningsresultanter[i][5]
        midtMom[i] = (M1 + M2) / 2

    # Legger til bidrag fra last
    for i in range(nlast):
        id = int(last[i][0])
        L = elementlengder[id]
        q1 = last[i][1]
        q2 = last[i][2]

    # Bruker formel for midtmoment og legger til midtmoment for hver trekantlast fra q1 og q2
    midtMom[id] += q1 * (L / 2) / (6 * L) * (2 * L ** 2 - 3 * L * L / 2 + (L / 2) ** 2)
    midtMom[id] += q2 * (L / 2) / (6 * L) * (2 * L ** 2 - 3 * L * L / 2 + (L / 2) ** 2)

    for i in range(npunktlast):
        id = int(punktlast[i][0])
        P = punktlast[i][1]
        a = punktlast[i][2]
        L = elementlengder[id]

        if a == L / 2:
            midtMom[id] += P * L / 4
        else:
            pass

    return midtMom

def midtS(spenningsresultanter, nlast, last, nelem, elementlengder):
    midtSkjar = np.zeros(nelem)
    #Skjærkrefter midt for hvert element gitt fra spenningsresultantvektoren
    for i in range(nelem):
        midtSkjar[i] = spenningsresultanter[i][1]

    # Midtkrefter for bjelker med fordelt last
    for i in range(nlast):
        id = int(last[i][0])
        Q1 = spenningsresultanter[id][1]
        q1 = last[i][1]
        q2 = last[i][2]
        L = elementlengder[id]
        midtSkj = 1 / 8 * q1 * L + 3 / 2 * q2 * L - Q1
        midtSkjar[id] = midtSkj

    return midtSkjar

def boyespenning(midtMomenter, geo, S, nelem, elem, EI, EA):
    sigma = np.zeros((nelem, 3))

    for i in range(nelem):
        I = EI[i] / elem[i][2]
        M1 = S[i][2]
        M2 = S[i][5]
        Mmidt = midtMomenter[i]
        # Z for de ukile geometriene
        geom = elem[i][3]
        z = 0

        if geom == 1:
            z = geo[0][1] / 2
        elif geom == 2:
            z = geo[1][3] / 2
        elif geom == 3:
            z = geo[2][3] / 2
        elif geom == 4:
            z = geo[3][1] / 2
        elif geom == 5:
            z = geo[4][1] / 2

    # regner ut bøyespenningene
    sigma1 = M1 * z / I

    # print("sigma1", i , sigma1)
    sigma2 = M2 * z / I 
    sigmaM = Mmidt * z / I

    # Spenning pga aksialkraft
    A = EA[i] / elem[i][2]

    # print("elem", i, A)
    N = S[i][0]

    # print("S", i, S[i][0])
    sigmaN = N / A

    # Legger til største spenning i hver av endene
    sigma[i][0] = max(-sigma1 + sigmaN, sigma1 + sigmaN)
    sigma[i][1] = max(-sigmaM + sigmaN, sigmaM + sigmaN)
    sigma[i][2] = max(-sigma2 + sigmaN, sigma2 + sigmaN)

    return sigma

def maks_sigma(sigma, nelem, elem, geo):
    sigma_maks = np.zeros((len(geo), 3)) # [element nr, verdi, ende1/midt/ende2]

    for i in range(nelem):
        geom = int(elem[i][3]) - 1 # indeksering i tverrsnitt/geomentri begynner p˚a 1

    for j in range(3):
        if abs(sigma[i][j]) > sigma_maks[geom][1]:
            sigma_maks[geom][0] = i
            sigma_maks[geom][1] = sigma[i][j]
            sigma_maks[geom][2] = j

    return sigma_maks 
