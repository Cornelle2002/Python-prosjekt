import numpy as np

from tverrsnitt import *

def sigma_flyt(max_m, max_n, nelem, elem, geo, EI, EA):

    #Lage tomme lister for spenninger i ulike profiler
    sigma_i = []                #I
    sigma_k = []                #Boks 
    sigma_ho = []               #Horisontal ror ---
    sigma_ver = []              #Diagonal/vertikal rør /\
    sigma_jack = []             #Ytre rør /\
    
    for el in range(nelem):
        moment = max_m[el]      #Finner maksmoment i elementet
        normal = max_n[el]      #Finner maks normalkraft i elementet
        E = elem[el][2]         #Finner E-modul tilsvarende elementet
        ei = EI[el]             #EI for elementet 
        ea = EA[el]             #EA for elementet

        I = ei/E                #I for elementet
        A = ea/E                #A for elementet

        geo_nr = elem[el][3]    #Geometri for elementet
        z = 0

        if geo_nr == 1: # geomentri 1
            z = int(geo[0][1])/2
            sigma_ho.append((moment/I) * z + (normal/A))
        elif geo_nr == 2: # geomentri 2
            z = int(geo[1][1])/2
            sigma_jack.append((moment/I) * z + (normal/A))
        elif geo_nr == 3: # geomentri 3
            z = int(geo[2][1])/2
            sigma_ver.append((moment/I) * z + (normal/A))
        elif geo_nr == 4: # geomentri 4
            z = int(geo[3][3])/2
            sigma_k.append((moment/I) * z + (normal/A))
        elif geo_nr == 5: # geomentri 5
            z = int(geo[4][3] + (2*geo[4][5]))/2
            sigma_i.append((moment/I) * z + (normal/A))
        

    return sigma_ho, sigma_jack, sigma_ver, sigma_k, sigma_i