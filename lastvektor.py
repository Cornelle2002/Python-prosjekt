import numpy as np

from verktøy import *
from matriser import *

def lastvektor(r, npunkt, punkt, nelem, elem): 
    R = np.zeros(npunkt * 3)                   # Lager liste med 3 frihetsgrader [N, S, M] per knutepunkt
    
    for i in range(nelem):                     # Itererer gjennom antall elementer
        theta = vinkel(elem[i], punkt)         # Finner vinkel i globalt system

        #Finner fastinnspeening for hvert element
        #temp_r = np.dot(r[i], transformasjonsmatrise(theta))
        #(Når vi prøvde å gjøre dett fikk vi feilmelding, så vi fikk tips fra en studass om at dette kunne funke)
        temp_r = np.dot(np.transpose(r[i]), np.transpose(transformasjonsmatrise(theta)))
    
        k_1 = int(elem[i][0])
        k_2 = int(elem[i][1]) 

        
        for j in range(3): #Iterer gjennom [N, S, M]
            index = (3 * k_1) + j              #Legger til bidraget til knutepunkt 1
            R[index] += temp_r[j]
            index = (3 * k_2) + j              #Legger til bidraget til knutepunkt 1
            R[index] += temp_r[j + 3] 

    return R # Returnerer lastvektor med informasjon om hvert knutepunkt

def punktkrafeter(elem, npunkt, punkt, npunlast, punlast, elementlengder):
    R1 = np.zeros(npunkt*3)                    # Lager liste med 3 frihetsgrader [N, S, M] per knutepunkt

    for i in range(npunlast):                  # Itererer gjennom antall punktlast

        element = int(punlast[i][0])           #Finner elemetet punktlasten virker på
        a = int(punlast[i][2])                 #Finner lengden fra knutepunkt 1 til hvor P vireker
        l = int(elementlengder[element])       #Finner lengden for elementet
        start = int(elem[element][0])          #Finner finner knutepunkt 1
        slutt = int(elem[element][1])          #Finner finner knutepunkt 2

        
        if a == 0:                             #Sjekker om lengden virker rett på knutepunkt 1
            n = (start) * 3 + 1
            R1[n] = int(punlast[i][1])         #Legger til nødvendlige skjærkrefter
        elif a == l:                           #Sjekker om lengden virker rett på knutepunkt 2
            n = (slutt) * 3 + 1
            R1[n] = int(punlast[i][1])         #Legger til nødvendlige skjærkrefter

    return R1 # Returnerer lastvektor med informasjon om hvert knutepunkt
              # Vi vet ikke om denne funksjonen egentlig er nødvendig, 
              # men var ment å fikse en neglisjering av en skjærkraft i lastvektor()