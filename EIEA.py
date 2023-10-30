from tverrsnitt import *

def ei(nelem, elem, geo):
    EI = [] # Oppretter en tom liste 

    for i in range(0, nelem): # ittererer gjennom antall elementer
        E = elem[i][2] # Finner E-Modul for element
        geo_nr = elem[i][3] # finner valgt geomentri for element
        I = 0

        try:
            if geo_nr == 1: # geomentri/tverrsnitt 1
                I = i_ror(geo[0][1], geo[0][2])
            elif geo_nr == 2: # geomentri/tverrsnitt 2
                I = i_ror(geo[1][1], geo[1][2])
            elif geo_nr == 3: # geomentri/tverrsnitt 3 
                I = i_ror(geo[2][1], geo[2][2])
            elif geo_nr == 4: # geomentri/tverrsnitt 4
                I = i_ror(geo[3][3], geo[3][4], geo[3][6])
            elif geo_nr == 5: # geomentri/tverrsnitt 5
                I = i_ror(geo[4][3], geo[4][4], geo[4][5], geo[4][6])
        
        except ValueError:
            print("Geometri ikke funnet")
        EI.append(E * I) # Legger til EI for hvert element

    return EI 

def ea(nelem, elem, geo):
    EA = []

    for i in range(0, nelem): # ittererer gjennom antall elementer
        E = elem[i][2] # Finner E-Modul for element
        geo_nr = elem[i][3] # finner valgt geomentri for element
        A = 0
        try:
            if geo_nr == 1: # geomentri/tverrsnitt 1
                A = ((np.pi * geo[0][1]**2)/4 - (np.pi * (geo[0][1]-geo[0][2])**2)/4)
            elif geo_nr == 2: # geomentri/tverrsnitt 2
                A = ((np.pi * geo[1][1]**2)/4 - (np.pi * (geo[1][1]-geo[1][2])**2)/4)
            elif geo_nr == 3: # geomentri/tverrsnitt 3
                A = ((np.pi * geo[2][1]**2)/4 - (np.pi * (geo[2][1]-geo[2][2])**2)/4)
            elif geo_nr == 4: # geomentri/tverrsnitt 4
                A = ((geo[3][3]*geo[3][4]) - ((geo[3][3]-geo[3][6])*(geo[3][4]-geo[3][6])))
            elif geo_nr == 5: # geomentri/tverrsnitt 5
                A = (geo[4][3] * geo[4][6]) + ((geo[4][4] - geo[4][6])*geo[4][5]) * 2
            
        except ValueError:
            print("Geometri ikke funnet")
            EA.append(E * A) # Legger til EA for hvert element i den tomme listen

    return EA