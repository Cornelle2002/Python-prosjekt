import numpy as np

def lengder(knutepunkt, element, nelem):
 
    elementlengder = np.zeros((nelem, 1))    #Lager en tomm liste for elementlengder
    
    for i in range (0, nelem):
        # OBS! Grunnet indekseringsyntaks i Python-arrays vil ikke denne funksjonen fungere naar vi bare har ett element.
        dx = knutepunkt[int(element[i][0])][0] - knutepunkt[int(element[i][1])][0]  #Regner ut avstand i x retning #Regner ut avstand i x retning mellom knutepunktene
        dy = knutepunkt[int(element[i][0])][1] - knutepunkt[int(element[i][1])][1]  #Regner ut avstand i y retning #Regner ut avstand i y retning mellom knutepunktene 
        elementlengder[i] = np.sqrt(dx*dx + dy*dy)  #Beregner elementlengder med Pythagoras' læresetning
 
    return elementlengder


def vinkel(elem, punkt): 
    p1 = int(elem[0]) # Finner punkt ende 1
    p2 = int(elem[1]) # Finner punkt ende 2
    dy = punkt[p2][1] - punkt[p1][1] # finner y-avstand mellom punktene
    dx = punkt[p2][0] - punkt[p1][0] # finne x-avstand mellom punktene
    theta = np.arctan2(dy, dx) #Finner vinkel ved bruk av arctan
    
    return theta