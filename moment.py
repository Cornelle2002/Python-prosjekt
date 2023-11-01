import numpy as np

def moment(nelem, elem, nlast, last, npunlast, punlast, geo, elementlengder):
    fim = np.zeros((nelem, 2))
    fisk = np.zeros((nelem, 2))

    for i in range(0, nlast):
        nr = int(last[i][0])

        d = geo[int(elem[i][3]) - 1][1] # Finner diameter for skalering av lastene
        q1 = last[i][1] * d / 1.5 # Skalerer lastene
        q2 = last[i][2] * d / 1.5

        l = elementlengder[nr] # finner elementlengden lasten virker på
        
        # Regner ut fastinnspennningsmoment for lokal ende 1 og 2
        Mab = -1 / 20 * (q2 - q1) * l ** 2 #Deler q opp i et kvadrat og en trekant ...
        Mba = 1 / 30 * (q2 - q1) * l ** 2 #... som starter der kvadratet slutter
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

    for i in range(0, npunlast): # Ittererer gjennom hver punktlast
        nr = int(punlast[i][0]) # finner ID til fordelt last
        P = punlast[i][1] # finner lastveriden
        a = punlast[i][2] # finner avstanden den virker fra ende 1
        L = elementlengder[nr] # finner lengden av elementet punktlasten virker på
        b = L - a # finner lengden fra ende 2

        Mab = -(P * a * b ** 2) / (L ** 2) #Bruker formelen for punnktlast
        Mba = (P * a ** 2 * b) / (L ** 2)
        Q1 = (P * b - Mab - Mba) / L
        Q2 = (P - Q1)

        fim[nr][0] += Mab
        fim[nr][1] += Mba
        fisk[nr][0] += Q1
        fisk[nr][1] += Q2
    
    return fim, fisk