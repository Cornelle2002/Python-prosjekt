import numpy as np

def fastinnspenningskrefter(nelem, elem, nlast, last, npunlast, punlast, geo, elementlengder):
    r = []
    for i in range(nelem):
        r.append([0, 0, 0, 0, 0, 0])

    for i in range(nlast):
        nr = int(last[i][0])
        d = geo[int(elem[i][3]) - 1][1]
        q1 = last[i][1] * d / 1.5
        q2 = last[i][2] * d / 1.5
        l = elementlengder[int(last[i][0])]

        fim_ab = -1 / 20 * q1 * l ** 2
        fim_ba = 1 / 30 * q1 * l ** 2

        fim_ab += -1 / 30 * q2 * l ** 2
        fim_ba += 1 / 20 * q2 * l ** 2

        fis_2 = (fim_ab + fim_ba + (1/2 * q2 * 2/3 * l ** 2) + (1/2 * q1 * 1/3 * l ** 2)) / l
        fis_1 = (1/2 * q1 *l) + (1/2 * q2 *l) - fis_2

        r[nr][1] += float(fis_1)
        r[nr][2] += float(fim_ab)
        r[nr][4] += float(fis_2)
        r[nr][5] += float(fim_ba)


    for i in range(npunlast):
        nr = int(punlast[i][0])
        P = punlast[i][1]
        a = punlast[i][2]
        l = elementlengder[int(punlast[i][0])]
        b = l - a

        fim_ab = -(P * a * (b ** 2)) / (l ** 2)
        fim_ba = (P * (a ** 2) * b) / (l ** 2)

        fis_2 = (fim_ab + fim_ba + (P * a)) / l
        fis_1 = (P - fis_2)

        r[nr][1] += -float(fis_1)
        r[nr][2] += -float(fim_ab)
        r[nr][4] += -float(fis_2)
        r[nr][5] += -float(fim_ba)

    return r