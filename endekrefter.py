import numpy as np

from matriser import *
from verktøy import *


def endekrefter(punkt, nelem, elem, L, r, EI, EA):
    endeK = np.empty((nelem, 6)) #Lager en tom liste

    for i in range(nelem):
        n1 = int(elem[i][0])    #Henter ut knutepunktene
        n2 = int(elem[i][1])    

        L_1 = L[(n1 * 3) : ((n1 * 3) + 3)]      #Henter ut deformasjoenen fra knutepunktene
        L_2 = L[(n2 * 3) : ((n2 * 3) + 3)]

        L_tot = np.zeros(6)         #Lager en en null liste

        for n in range(0, 2):       #Putter deformasjonen inn på riktig plass
            L_tot[n] = L_1[n]

        for m in range(0, 2):
            L_tot[m + 2] = L_2[m]
            
        theta = vinkel(elem[i], punkt)      #Henter globale vinkelen til elementet
        T = transformasjonsmatrise(theta)       #Henter ut transformasjonsmatrisen med hensyn på global vinkel

        L_tot = T*np.transpose(np.matrix(L_tot))        #Transformerer lokal lastvektor

        temp_r = np.transpose(np.matrix(r[i]))      #Transformerer lokal fastinnspeningskrefter
        k = np.matrix(lokal_matrise(EI[i], EA[i], L[i]))    #Henter lokal stivhetsmatrise

        S = k * L_tot + temp_r      #Regner ut elementets ende krefter for hvert knutepunkt
 
        endeK[i] = np.array(np.transpose(S))    # Setter det inn på riktig plass i listen med endekrefter

    return endeK    #Returnerer matrisen med alle endekreftene for alle elementene
