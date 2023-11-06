import numpy as np

from endemoment import *


def max_moment(endem, nelem, elem, nlast, last, npunlast, punlast, elementlengder):
    m_tot = np.zeros(nelem)
    
    for el in range(nlast):
        #Liste for å holde moment for hver iterasjon
        temp_m = []

        #Henter fordeltlast i elementets knutepunkt og elementlengde
        nr = int(last[el][0])
        l = elementlengder[nr]
        q_1 = int(last[el][1])
        q_2 = int(last[el][2])
        
        #Henter [N1, S1, M1, N2, S2, M2] for elementet som trengs
        Q1 = endem[el][1]
        M1 = endem[el][2]

        #Itererer over l
        x = np.linspace(0,l,1000)

        for temp_x in x:
            temp_m.append(abs(1/3 * q_1 * temp_x**2 + 1/6 *(q_1 + ((q_2 - q_1)/(l)) * temp_x) * temp_x**2 - Q1 * temp_x - M1))

        #Legger elementets max moment på riktig plass i total listen
        if m_tot[nr] != 0:
            print('Error: For mange ytre krefter')
        
        m_tot[nr] = max(temp_m)
        
    for el in range(npunlast):
        #Liste for å holde moment for hver iterasjon
        temp_m = []

        #Henter punktlast, elementlengde og lengden fra knutepunkt 1
        nr = int(punlast[el][0])
        l = elementlengder[nr]
        P = int(punlast[el][1])
        a = int(punlast[el][2])
        
        #Henter [N1, S1, M1, N2, S2, M2] for elementet som trengs
        Q1 = endem[el][1]
        M1 = endem[el][2]

        #Itererer over l
        x = np.linspace(0,l,1000)

        for temp_x in x:
            if temp_x < a:
                temp_m.append(abs(P * (temp_x - a) - Q1 * temp_x - M1))
            else:
                temp_m.append(abs(-Q1 * temp_x - M1))

        #Legger elementets max moment på riktig plass i total listen
        if m_tot[nr] != 0:
            print('Error: For mange ytre krefter på et elemet')
        
        m_tot[nr] = max(temp_m)
    
    for el in range(nelem):
        #Hopper over elementer som allerede har verdier
        if (m_tot[el] != 0):
            continue

        #Liste for å holde moment for hver iterasjon
        temp_m = []

        #Henter elementlengden
        nr = int(el)
        l = elementlengder[nr]
        
        #Henter [N1, S1, M1, N2, S2, M2] for elementet som trengs
        Q1 = endem[el][1]
        M1 = endem[el][2]

        #Itererer over l
        x = np.linspace(0,l,1000)

        for temp_x in x:
            temp_m.append(abs(-M1 - Q1 * temp_x))

        #Legger elementets max moment på riktig plass i total listen
        
        m_tot[nr] = max(temp_m)
        
    return m_tot

def max_skjaer(nelem, endem):

    q_tot = np.zeros(nelem)

    for i in range(nelem):
        if abs(endem[i][1]) >= abs(endem[i][4]):
            q_tot[i] = abs(endem[i][1])
        else:
            q_tot[i] = abs(endem[i][4])

    return q_tot
        

def max_aksial(nelem, endem):

    n_tot = np.zeros(nelem)

    for i in range(nelem):
        n_tot[i] = abs(endem[i][0])

    return n_tot
    



  