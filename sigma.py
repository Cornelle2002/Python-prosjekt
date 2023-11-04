import numpy as np

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
        geom = int(elem[i][3]) - 1 # indeksering i tverrsnitt/geomentri begynner på 1

    for j in range(3):
        if abs(sigma[i][j]) > sigma_maks[geom][1]:
            sigma_maks[geom][0] = i
            sigma_maks[geom][1] = sigma[i][j]
            sigma_maks[geom][2] = j

    return sigma_maks