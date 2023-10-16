import numpy as np


filnavn = 'text.txt'

def elementadata(filnavn):
    data = []

    start_print = False

    with open(filnavn, 'r') as fil:
        linjer = fil.readlines()

    for line in linjer:
        if 'Element:' in line:
            start_print = True
            continue

        if start_print:
            if not line.strip():
                break

            # Fjern eventuelle ekstra mellomrom og linjeskift
            elementer = line.strip().split(', ')
            #Legger de to første, som utgjør elementet i listen data. og elementene bak, som inneholder bjelkeinfo i listen til de to første. liste i liste
            element_1 = int(elementer[0])
            element_2 = int(elementer[1])
            egenskaper = [int(elementer[2]), elementer[3], int(elementer[4]), int(elementer[5])]
            if elementer[3] == 'i':
                egenskaper = [int(elementer[2]), elementer[3], int(elementer[4]), int(elementer[5]), int(elementer[6]), int(elementer[7])]
                #Listen med de element, og geometri osv samles alle i data
            elementene = [element_1, element_2, egenskaper]
            data.append(elementene)

    return data


# resultat = elementadata(filnavn)
# for rad in resultat:
#     print(rad)
    # print(rad[2][0]) #EKSEMPEL: Hvordan hente ut E-modul fra listen 


#Lag også en funksjon som beregner bøyestivheten for elementene på bakgrunn av tverrsnittsdata.
def bøyestivhet(Elementnr):
    x = elementadata(filnavn)
    x = x[Elementnr]
    if x[2][1] == 'c':
        E = x[2][0]
        I = (np.pi/64)*(x[2][3]**4-x[2][2]**4)
    else:
        E = x[2][0]
        I_flens = 2*(1/12*x[2][4]*x[2][5]**3)
        I_steg = (1/12*x[2][2]*x[2][3]**3)
        I = I_flens + I_steg
    return E*I

# print(bøyestivhet(14))