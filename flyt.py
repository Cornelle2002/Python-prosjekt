import numpy as np

from tverrsnitt import *

def sigma_flyt(max_m, max_n, nelem, elem, geo, EI, EA):
    sigma = np.zeros(nelem)
    
    for el in range(nelem):
        moment = max_m[el]
        print(moment)
        normal = max_n[el]
        print(normal)
        E = elem[el][2]
        ei = EI[el]
        ea = EA[el]

        I = ei/E
        print(I)
        A = ea/E
        print(A)

        geo_nr = elem[el][3]
        z = 0

        if geo_nr == 1: # geomentri 1
            z = int(geo[0][1])/2
        elif geo_nr == 2: # geomentri 2
            z = int(geo[1][1])/2
        elif geo_nr == 3: # geomentri 3
            z = int(geo[2][1])/2
        elif geo_nr == 4: # geomentri 4
            I = int(geo[3][3])/2
        elif geo_nr == 5: # geomentri 5
            I = int(geo[4][3])/2
        
        sigma[el] = ((moment/I) * z + (normal/A))

    return sigma