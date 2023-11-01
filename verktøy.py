import numpy as np
from tabulate import tabulate

def lengder(knutepunkt, element, nelem):
 
    elementlengder = np.zeros((nelem, 1))
    # Beregner elementlengder med Pythagoras' læresetning
    for i in range (0, nelem):
        # OBS! Grunnet indekseringsyntaks i Python-arrays vil ikke denne funksjonen fungere naar vi bare har ett element.
        dx = knutepunkt[int(element[i][0])][0] - knutepunkt[int(element[i][1])][0]
        dy = knutepunkt[int(element[i][0])][1] - knutepunkt[int(element[i][1])][1]
        elementlengder[i] = np.sqrt(dx*dx + dy*dy)
 
    return elementlengder


def vinkel(elem, punkt): 
    p1 = int(elem[0]) # Finner punkt ende 1
    p2 = int(elem[1]) # Finner punkt ende 2
    dy = punkt[p2][1] - punkt[p1][1] # finner y-avstand mellom punktene
    dx = punkt[p2][0] - punkt[p1][0] # finne x-avstand mellom punktene
    theta = 0

    if punkt[p1][0] == punkt[p2][0] and dy > 0: # lik y-verdi gir 90 grader n˚ar dy > 0

        theta = np.pi / 2

    elif punkt[p1][0] == punkt[p2][0] and dy < 0: # lik y-verdi gir -90 grader n˚ar dy < 0
        theta = -np.pi / 2

    elif dy < 0: # n˚ar dy < 0 regnes theta ut med trigonometri 
        theta = np.arctan2(dy, dx) + np.pi

    else: 22
    theta = np.arctan2(dy, dx)

    return theta # Returnerer vinkelen i radianer

def print_fint(list, elem):
    liste = []
    for i in range(len(list)):
        liste.append([int(elem[i][0]),list[i]])
    print(tabulate(liste))
    