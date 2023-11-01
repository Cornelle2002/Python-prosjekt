import numpy as np

def moment(nelem, elem, nlast, last, npunlast, punlast, geo, elementlengder):
    fim = np.zeros((nelem, 2))
    fisk = np.zeros((nelem, 2))

    for i in range(nlast):
        nr = int(last[i][0])
        d = geo[int(elem[i][3]) - 1][1]
        q1 = last[i][1] * d / 1.5
        q2 = last[i][2] * d / 1.5
        l = elementlengder[nr]

        Mab = -1 / 20 * (q2 - q1) * l ** 2
        Mba = 1 / 30 * (q2 - q1) * l ** 2
        Mab += -1 / 30 * (q2 - q1) * l ** 2
        Mba += 1 / 20 * (q2 - q1) * l ** 2
        Q1 = q1 * l * (7 / 20)
        Q2 = q1 * l * (3 / 20)
        Q1 += q2 * l * (3 / 20)
        Q2 += q2 * l * (7 / 20)

        fim[nr][0] += Mab
        fim[nr][1] += Mba
        fisk[nr][0] += Q1
        fisk[nr][1] += Q2

    for i in range(npunlast):
        nr = int(punlast[i][0])
        P = punlast[i][1]
        a = punlast[i][2]
        L = elementlengder[nr]
        b = L - a

        Mab = -(P * a * b ** 2) / (L ** 2)
        Mba = (P * a ** 2 * b) / (L ** 2)
        Q1 = (P * b - Mab - Mba) / L
        Q2 = (P - Q1)

        fim[nr][0] += Mab
        fim[nr][1] += Mba
        fisk[nr][0] += Q1
        fisk[nr][1] += Q2

    return fim, fisk