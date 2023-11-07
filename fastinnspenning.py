import numpy as np

def fastinnspenningskrefter(nelem, elem, nlast, last, npunlast, punlast, geo, elementlengder):
    
    #Lager tom liste
    r = []

    #Lager plass til [N1, S1, M1, N2, S2, M2] for hvert elemenent
    for i in range(nelem):
        r.append([0, 0, 0, 0, 0, 0])
    
    #Finner fast innspenningsmoment og fast innspenningsskjær med hensyn på fordelt
    for i in range(nlast):
        nr = int(last[i][0])                #Henter ut elementet lasten virker på
        l = elementlengder[int(last[i][0])] #Finner lengden på elementet
        d = geo[int(elem[nr][3])][1]        #Finner diameter for tverssnittet til elementet
        q1 = last[i][1] * d / 1500          #Regner ut verdi for fordelt last i ende 1 for elementet
        q2 = last[i][2] * d / 1500          #Regner ut verdi for fordelt last i ende 2 for elementet
        
        #Regner ut fastinnspenningsmoment vha to trekantlaster
        fim_ab = -1 / 20 * q1 * l ** 2      #Henter fra Tabell 8.3 fastinnspenningsmomenter fra kompendiet
        fim_ba = 1 / 30 * q1 * l ** 2       
        
        fim_ab += -1 / 30 * q2 * l ** 2     
        fim_ba += 1 / 20 * q2 * l ** 2      
        
        #Regner ut fastinnspenningsskjærkraft for ende 1 og ende 2
        fis_2 = (fim_ab + fim_ba + (1/2 * q2 * 2/3 * l ** 2) + (1/2 * q1 * 1/3 * l ** 2)) / l   #Superposisjon
        fis_1 = (1/2 * q1 *l) + (1/2 * q2 *l) - fis_2                                           

        r[nr][1] += float(fis_1)    #Legger til fastinnspenningskjær ende 1
        r[nr][2] += float(fim_ab)   #Legger til fastinnspenningsmoment ende 1
        r[nr][4] += float(fis_2)    #Legger til fastinnspenningskjær ende 2
        r[nr][5] += float(fim_ba)   #Legger til fastinnspenningsmoment


    for i in range(npunlast):
        nr = int(punlast[i][0])                 #Henter ut elementet punktlasten virker på
        P = punlast[i][1]                       #Finner intensitet for punktlast
        l = elementlengder[int(punlast[i][0])]  #Finner lengden på elementet
        a = punlast[i][2]                       #Finner ut avstand fra ende 1 på elementet til punktlasten
        b = l - a                               #----------------------------\\---------------------------

        fim_ab = -(P * a * (b ** 2)) / (l ** 2) #Henter fra Tabell 8.3 fastinnspenningsmomenter fra kompendiet
        fim_ba = (P * (a ** 2) * b) / (l ** 2)

        fis_2 = (fim_ab + fim_ba + (P * a)) / l #Superposisjon
        fis_1 = (P - fis_2)

        r[nr][1] += -float(fis_1)   #Legger til fastinnspenningskjær ende 1
        r[nr][2] += -float(fim_ab)  #Legger til fastinnspenningsmoment ende 1
        r[nr][4] += -float(fis_2)   #Legger til fastinnspenningskjær ende 2
        r[nr][5] += -float(fim_ba)  #Legger til fastinnspenningsmoment ende 2

    return r