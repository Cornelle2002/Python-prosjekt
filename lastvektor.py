import numpy as np

def vinkel(element, punkt): 
    p1 = element[0] # Finner punkt ende 1
    p2 = element[1] # Finner punkt ende 2
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



def lastvektor(fim, npunkt, punkt, nelem, elem):
    
    return