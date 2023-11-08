import math
import numpy as np
import matplotlib.pyplot as plt

def plot(temp, temp_x, nr, ax, col, row):
    ax[row, col].plot(temp_x, temp) #Plotter verdiene for x og y akse
    ax[row, col].hlines(i=0, xmin=0, xmax=np.max(temp_x), colors='r', linestyles='--', lw=0.5) #Plotter base linjen
    ax[row, col].set_title(str(nr), fontsize=10) #Setter titel som element nummer
    ax[row, col].set_xlabel("[m]", fontsize=8) #Setter x-aksen lik meter

def plotting(endeK, nelem, nlast, last, npunlast, punlast, elementlengder):
    #Velger formatet plotene kommer i
    cols = 6
    rows = nelem//cols

    if nelem % cols != 0:
        rows += 1

    if rows == 0:
        rows += 1

    #Setter opp subplots
    mom_fig, ax = plt.subplots(rows, cols, squeeze=False)
    mom_fig.suptitle("Momentdiagram for element [Nm]") #Plotter overskrift
    mom_fig.tight_layout(pad=1.0)

    skj_fig, bx = plt.subplots(rows, cols, squeeze=False)
    skj_fig.suptitle("Skjærkraftdiagram for element [N]")
    skj_fig.tight_layout(pad=1.0)

    nor_fig, cx = plt.subplots(rows, cols, squeeze=False)
    nor_fig.suptitle("Normalkraft for element [N]")
    nor_fig.tight_layout(pad=1.0)

    it_elem = [] #Tom liste for elemeter

    #Itterer gjennom elementer med fordelt last
    for x in range (nlast):
        # Legger element nummeret i it_elem listen
        nr = int(last[x][0])
        it_elem.append(nr)
    
        #Midlertidig liste for moment, skjærkraft og normalkraft
        temp_m = []
        temp_s = []
        temp_n = []

        #Henter elementlengde
        l = elementlengder[nr]

        #Lager en linspace som gir oss 1000 x verdier fra 0 til L
        temp_x = np.linspace(0,l,1000)

        #Henter ut fordelt last i knutepunkt 1 og 2
        q_1 = last[x][1]
        q_2 = last[x][2]


        #Henter ut N1, Q1 og M1 for elementet
        N1 = endeK[nr][0]
        Q1 = endeK[nr][1]
        M1 = endeK[nr][2]

        #Regner ut endekreftene for elementet fra knutepunkt 1 til knutepunkt 2
        for i in temp_x:
            temp_m.append(1/3 * q_1 * i**2 + 1/6 *(q_1 + ((q_2 - q_1)/(l)) * i) * i**2 - Q1 * i - M1)
            temp_s.append(q_1 * i + ((q_2 - q_1)/(2*l))* i**2 - Q1)
            temp_n.append(-N1)


        #Finner posisjonen til diagrammet
        row = int(math.ceil((nr + 1)/cols)) - 1
        col = int(nr + 1 - (row)* cols) - 1

        # Bruker plot funksjonen til å plotte verdiene
        plot(temp_m, temp_x, nr, ax, col, row)
        plot(temp_s, temp_x, nr, bx, col, row)
        plot(temp_n, temp_x, nr, cx, col, row)


    #Itterer gjennom elementer med punktlast
    #Mye av denne for-løkken er satt opp lit som den for fordelt last
    for x in range(npunlast):
        # Legger element nummeret i it_elem listen
        nr = int(punlast[x][0])
        it_elem.append(nr)

        temp_m = []
        temp_s = []
        temp_n = []

        nr = int(punlast[x][0])
        l = elementlengder[nr]
        temp_x = np.linspace(0,l,1000)

        #Henter ut punktlaste og lengden fra knutepunkt 1
        P = int(punlast[x][1])
        a = int(punlast[x][2])

        N1 = endeK[nr][0]
        Q1 = endeK[nr][1]
        M1 = endeK[nr][2]

        #Regner ut endekreftene for elementet fra knutepunkt 1 til knutepunkt 2
        #Bytter formeler når i verdien er større enn a
        for i in temp_x:
            if (i > a):
                temp_m.append(P * (i - a) - Q1 * i - M1)
                temp_s.append(P - Q1)
                temp_n.append(-N1)

            else:
                temp_m.append(-Q1 * i - M1)
                temp_s.append(-Q1)
                temp_n.append(-N1)

        row = int(math.ceil((nr + 1)/cols)) - 1
        col = int(nr + 1 - (row)* cols) - 1

        plot(temp_m, temp_x, nr, ax, col, row)
        plot(temp_s, temp_x, nr, bx, col, row)
        plot(temp_n, temp_x, nr, cx, col, row)

    #Itterer gjennom alle elementene som ikke er allerede utregnet
    for x in range(nelem):
        #Kjører koden for alle elmenter som ikke er utregnet
        for j in it_elem:
            if (x == j):
                continue

        temp_m = []
        temp_s = []
        temp_n = []

        nr = x #x er lik alle elementer som ikker allerede utregnet
        l = elementlengder[nr]
        temp_x = np.linspace(0,l,1000)

        N1 = endeK[nr][0]
        Q1 = endeK[nr][1]
        M1 = endeK[nr][2]

        #Regner ut endekreftene for elementet fra knutepunkt 1 til knutepunkt 2
        for i in temp_x:
            temp_m.append(-M1 - Q1 * i)
            temp_s.append(-Q1)
            temp_n.append(-N1)

        row = int(math.ceil((nr + 1)/cols)) - 1
        col = int(nr + 1 - (row)* cols) - 1

        plot(temp_m, temp_x, nr, ax, col, row)
        plot(temp_s, temp_x, nr, bx, col, row)
        plot(temp_n, temp_x, nr, cx, col, row)
        
    return 0