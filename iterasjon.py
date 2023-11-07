from tverrsnitt import *

def iterasjon(sigma, nelem, elem, geo):
    ele_ho = []
    ele_jack = []
    ele_ver = []
    ele_k = []
    ele_i = []

    for i in range(nelem):
        geo_nr = elem[i][3]
        if geo_nr == 1: # geomentri 1
            ele_ho.append(i)
        elif geo_nr == 2: # geomentri 2
            ele_jack.append(i)
        elif geo_nr == 3: # geomentri 3
            ele_ver.append(i)
        elif geo_nr == 4: # geomentri 4
            ele_k.append(i)
        elif geo_nr == 5: # geomentri 5
            ele_i.append(i)

    #Maks flyt for hvert materiale 
    #(Vi antok at maks flyt kom til å være konstat, så disse blir ikke lest inn)
    fy_al = 250000000
    fy_st = 420000000

    fy_al_inn = (fy_al * 8)/10
    fy_st_inn = (fy_st * 8)/10

    E_al = 70000000000
    E_st = 210000000000

    max_fy = []
    max_fy_nr = []

    for i in range(len(sigma)):
        max_fy.append(max(sigma[i]))
        max_fy_nr.append(np.argmax(sigma[i]))


    tver_ho = []
    tver_jack = []
    tver_ver = []
    tver_k = []
    tver_i = []

    for el in range(len(geo)):
        if el == 0: # geomentri 1
            if elem[max_fy_nr[el]][2] == E_st:
                while max_fy[el] > fy_st_inn:
                    geo[0][2] += 1
                    if geo[0][2] == (geo[0][1]/2):
                        print('Geometri 1: Tykkelse overskrifer diameterens dimensjoner')
                        tver_ho.append(geo[0][1])
                        tver_ho.append(geo[0][2])
                        break
                else:
                    tver_ho.append(geo[0][1])
                    tver_ho.append(geo[0][2])
            else:
                while max_fy[el] > fy_al_inn:
                    geo[0][2] += 1
                    if geo[0][2] == (geo[0][1]/2):
                        print('Geometri 1: Tykkelse overskrifer diameterens dimensjoner')
                        tver_ho.append(geo[0][1])
                        tver_ho.append(geo[0][2])
                        break
                else:
                    tver_ho.append(geo[0][1])
                    tver_ho.append(geo[0][2])

        elif el == 1: # geomentri 2
            if elem[max_fy_nr[el]][2] == E_st:
                while max_fy[el] > fy_st_inn:
                    geo[1][2] += 1
                    if geo[1][2] == (geo[1][1]/2):
                        print('Geometri 2: Tykkelse overskrifer diameterens dimensjoner')
                        tver_jack.append(geo[1][1])
                        tver_jack.append(geo[1][2])
                        break
                else:
                    tver_jack.append(geo[1][1])
                    tver_jack.append(geo[1][2])
            else:
                while max_fy[el] > fy_al_inn:
                    geo[1][2] += 1
                    if geo[1][2] == (geo[1][1]/2):
                        print('Geometri 2: Tykkelse overskrifer diameterens dimensjoner')
                        tver_jack.append(geo[1][1])
                        tver_jack.append(geo[1][2])
                        break
                else:
                    tver_jack.append(geo[1][1])
                    tver_jack.append(geo[1][2])
            
        elif el == 2: # geomentri 3
            if elem[max_fy_nr[el]][2] == E_st:
                while max_fy[el] > fy_st_inn:
                    geo[2][2] += 1
                    if geo[2][2] == (geo[2][1]/2):
                        print('Geometri 3: Tykkelse overskrifer diameterens dimensjoner')
                        tver_ver.append(geo[2][1])
                        tver_ver.append(geo[2][2])
                        break
                else:
                    tver_ver.append(geo[2][1])
                    tver_ver.append(geo[2][2])
            else:
                while max_fy[el] > fy_al_inn:
                    geo[2][2] += 1
                    if geo[2][2] == (geo[2][1]/2):
                        print('Geometri 3: Tykkelse overskrifer diameterens dimensjoner')
                        tver_ver.append(geo[2][1])
                        tver_ver.append(geo[2][2])
                        break
                else:
                    tver_ver.append(geo[2][1])
                    tver_ver.append(geo[2][2])
            
        elif el == 3: # geomentri 4
            if elem[max_fy_nr[el]][2] == E_st:
                while max_fy[el] > fy_st_inn:
                    geo[3][6] += 1
                    if geo[3][6] == (geo[3][3]/2):
                        print('Geometri 4: Tykkelse overskrifer høyde dimensjoner')
                        tver_k.append(geo[3][3])
                        tver_k.append(geo[3][4])
                        tver_k.append(geo[3][6])
                        break
                else:
                    tver_k.append(geo[3][3])
                    tver_k.append(geo[3][4])
                    tver_k.append(geo[3][6])
            else:
                while max_fy[el] > fy_al_inn:
                    geo[3][6] += 1
                    if geo[3][6] == (geo[3][6]/2):
                        print('Geometri 4: Tykkelse overskrifer høyde dimensjoner')
                        tver_k.append(geo[3][3])
                        tver_k.append(geo[3][4])
                        tver_k.append(geo[3][6])
                        break
                else:
                    tver_k.append(geo[3][3])
                    tver_k.append(geo[3][4])
                    tver_k.append(geo[3][6])
            
        elif el == 4: # geomentri 5
            if elem[max_fy_nr[el]][2] == E_st:
                while max_fy[el] > fy_st_inn:
                    geo[4][5] += 1
                    geo[4][6] += 1
                    if geo[4][5] == (geo[4][3]):
                        print('Geometri 5: Tykkelse overskrifer stag høydens dimensjoner')
                        tver_i.append(geo[4][3])
                        tver_i.append(geo[4][4])
                        tver_i.append(geo[4][5])
                        tver_i.append(geo[4][6])
                        break
                else:
                    tver_i.append(geo[4][3])
                    tver_i.append(geo[4][4])
                    tver_i.append(geo[4][5])
                    tver_i.append(geo[4][6])
            else:
                while max_fy[el] > fy_al_inn:
                    geo[4][5] += 1
                    geo[4][6] += 1
                    if geo[4][5] == (geo[4][3]):
                        print('Geometri 5: Tykkelse overskrifer stag høydens dimensjoner')
                        tver_i.append(geo[4][3])
                        tver_i.append(geo[4][4])
                        tver_i.append(geo[4][5])
                        tver_i.append(geo[4][6])
                        break
                else:
                    tver_i.append(geo[4][3])
                    tver_i.append(geo[4][4])
                    tver_i.append(geo[4][5])
                    tver_i.append(geo[4][6])



    tver_tot = [tver_ho, tver_jack, tver_ver, tver_k, tver_i]

    return tver_tot