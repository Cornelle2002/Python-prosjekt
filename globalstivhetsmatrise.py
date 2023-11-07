from verktøy import *
from matriser import *

def globalStivhetsmatrise(npunkt, punkt, nelem, elem, geo, EI, EA, L): 
    K =  np.zeros((3 * npunkt, 3 * npunkt))                 #Lager en 39*39 2D-liste med nuller
    
    for n in range(nelem):                                  # Itererer gjennom antall elementer

        glob = []                                           # Lager en tom liste for global frihetsgrad

        n1 = int(elem[n][0])                                # Henter ut elementets knutepunkt 1
        n2 = int(elem[n][1])                                # Henter ut elementets knutepunkt 2

        for j in range(3):                                  # Finner knutepunktet 1 globale frihetsgrad
            glob.append(3*(n1) + (j))
        
        for j in range(3):                                  # Finner knutepunktet 2 globale frihetsgrad
            glob.append(3*(n2) + (j))

        k = lokal_matrise(EI[n], EA[n], L[n])               # Henter lokal elementstivhetsmatrise
        theta = vinkel(elem[n], punkt)                      # Finner elementets globale vinkel
        T = transformasjonsmatrise(theta)                   # Finner tranformasjonsmatrisen basert op gobal vinkel
        k_g = np.transpose(T) @ k @ T                       # Regner ut den lokale stivhetsmatrisen

        for m in range(len(k_g)):                           # Finner posisjonene til komponentene fra lokale stivhetsmatrisen
                for o in range(len(k_g)):
                    K[glob[m]][glob[o]] += k_g.item(m,o)    # Summer/putter lokale komponenter inn i riktig posisjon av global stivhetsmatrisen

    return K # Returnerer global stivhetsmatrise 
