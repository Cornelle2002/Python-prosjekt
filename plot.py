import math
import numpy as np
import matplotlib.pyplot as plt

def plot_diagrams(temp, temp_x, nr, ax, col, row):
    ax[row, col].plot(temp_x, temp)
    ax[row, col].hlines(y=0, xmin=0, xmax=np.max(temp_x), colors='r', linestyles='--', lw=0.5)
    ax[row, col].set_title(str(nr), fontsize=10)
    ax[row, col].set_xlabel("Meter", fontsize=8)

def plotting(endeK, nelem, nlast, last, npunlast, punlast, elementlengder):
    #Lager oppsette for plottingen
    Cols = 6
    Rows = nelem//Cols

    if nelem % Cols != 0:
        Rows += 1

    if Rows == 0:
        Rows += 1


    mom_fig, ax = plt.subplots(Rows, Cols, squeeze=False)
    mom_fig.suptitle("Momentdiagram for element [Nm]")
    mom_fig.tight_layout(pad=1.0)

    skj_fig, bx = plt.subplots(Rows, Cols, squeeze=False)
    skj_fig.suptitle("Skjærkraftdiagram for element [N]")
    skj_fig.tight_layout(pad=1.0)

    normal_fig, cx = plt.subplots(Rows, Cols, squeeze=False)
    normal_fig.suptitle("Normalkraft for element [N] ")
    normal_fig.tight_layout(pad=1.0)

    it_elem = []

    #Itterer gjennom ellementer med fordelt last
    for x in range (nlast):
        nr = int(last[x][0])
        it_elem.append(nr)
    
        #Resultatarray for momenter, skjærkraft og normalkraft
        temp_m = []
        temp_s = []
        temp_n = []

        #Henter elementlengde
        l = elementlengder[nr]

        #Oppretter et array med x-verdier fra 0 til L med 1000 verdier
        temp_x = np.linspace(0,l,1000)

        #Henter ut inensiteten til den fordelte lasten
        q_1 = last[x][1]
        q_2 = last[x][2]


        #Henter ut Q1, M1 og M2 for bjelken
        N1 = endeK[nr][0]
        Q1 = endeK[nr][1]
        M1 = endeK[nr][2]

        #Regner ut momentet langs bjelken fra knutepunkt 1 til knutepunkt 2
        for y in temp_x:
            temp_m.append(1/3 * q_1 * y**2 + 1/6 *(q_1 + ((q_2 - q_1)/(l)) * y) * y**2 - Q1 * y - M1)
            temp_s.append(q_1 *y + ((q_2 - q_1)/(2*l))*y**2 - Q1)
            temp_n.append(-N1)


        #Finner posisjonen til diagrammet i vinduet 
        row = int(math.ceil((nr + 1)/Cols)) - 1
        col = int(nr + 1 - (row)* Cols) - 1

        plot_diagrams(temp_m, temp_x, nr, ax, col, row)
        plot_diagrams(temp_s, temp_x, nr, bx, col, row)
        plot_diagrams(temp_n, temp_x, nr, cx, col, row)


    #Lasttilfelle, punktlast
    for x in range(npunlast):
        nr = int(punlast[x][0])
        it_elem.append(nr)

        #Resultatarray for momenter
        temp_m = []
        temp_s = []
        temp_n = []

        #Henter elementlengde
        nr = int(punlast[x][0])
        l = elementlengder[nr]

        #Oppretter et array med x-verdier fra 0 til L med 1000 verdier
        temp_x = np.linspace(0,l,1000)

        #Henter ut kraften P:
        P = int(punlast[x][1])
        a = int(punlast[x][2])


        #Henter ut Q1, M1 og M2 for bjelkene
        N1 = endeK[nr][0]
        Q1 = endeK[nr][1]
        M1 = endeK[nr][2]


        for y in temp_x:
            if (y > a):
                temp_m.append(P * (y - a) - Q1 * y - M1)
                temp_s.append(P - Q1)
                temp_n.append(-N1)

            else:
                temp_m.append(-Q1 * y - M1)
                temp_s.append(-Q1)
                temp_n.append(-N1)


        #Finner posisjonen til diagrammet i vinduet 
        row = int(math.ceil((nr + 1)/Cols)) - 1
        col = int(nr + 1 - (row)* Cols) - 1

        plot_diagrams(temp_m, temp_x, nr, ax, col, row)
        plot_diagrams(temp_s, temp_x, nr, bx, col, row)
        plot_diagrams(temp_n, temp_x, nr, cx, col, row)

    
    #Ingen ytre last, bare endemomenter
    for x in range(nelem):
        #Sjekker om det allerede har blitt regnet med moment fra tidligere funksjon
        for i in it_elem:
            if (x == i):
                continue

        nr = x

        #Resultatarray for momenter
        temp_m = []
        temp_s = []
        temp_n = []


        #Henter elementnummer og lengde
        l = elementlengder[nr]

        #Oppretter et array med x-verdier fra 0 til L med 1000 verdier
        temp_x = np.linspace(0,l,1000)


        #Henter ut N1, Q1, Q2, M1 og M2 for bjelkene
        N1 = endeK[nr][0]
        M1 = endeK[nr][2]
        Q1 = endeK[nr][1]
        Q2 = endeK[nr][4]
        M2 = endeK[nr][5]


        #Regner ut verdier til momentdiagramet
        for y in temp_x:
            temp_m.append(-M1 - Q1 * y)
            temp_s.append(-Q1)
            temp_n.append(-N1)

        #Finner posisjonen til diagrammet i vinduet 
        row = int(math.ceil((nr + 1)/Cols)) - 1
        col = int(nr + 1 - (row)* Cols) - 1

        plot_diagrams(temp_m, temp_x, nr, ax, col, row)
        plot_diagrams(temp_s, temp_x, nr, bx, col, row)
        plot_diagrams(temp_n, temp_x, nr, cx, col, row)
        

    return 0