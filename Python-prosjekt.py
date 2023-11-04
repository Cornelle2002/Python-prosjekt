from lesinput import *
from structure_visualization import *
from verktøy import *
from fastinnspenning import *
from lastvektor import *
from globalstivhetsmatrise import *
from randbetingelser import *
from deformasjon import *
from Endemoment import *
from EIEA import *
from sigma import *


# -----Rammeanalyse-----
def main():
    # -----Initialiserer figurer-----
    fig_init, ax_init, fig_def, ax_def = setup_plots()
     
    # -----Til visualiseringen, velg første indeks brukt i nummerering av noder og element-----
    first_index = 0
 
    # -----Leser input-data-----
    file = 'input.txt'
    k, e, f_l, p, g, nk, ne, nf_l, npu = input(file)
 
    #Kaller funksjonen og lagrer oppdatert resultat med riktig verdier                           
    punkt = float_char(k)
    elem = float_char(e)
    last = float_char(f_l) 
    punlast = float_char(p)
    geometri = float_char(g)
    npunkt = nk
    nelem = ne
    nlast = nf_l 
    npunlast = npu

    # -----Plott initalramme-----
    plot_structure(ax_init, punkt, elem, 1, first_index, file)

    # -----Regner ut lengder til elementene------
    elementlengder = lengder(punkt, elem, nelem)
 
    # -----Fastinnspenningsmomentene------
    fim, fisk = fastinnspenningskrefter(nelem, elem, nlast, last, npunlast, punlast, geometri, elementlengder)
    #print(len(fim))
    #print(len(fisk))
    #print(fim)
    #print(fisk)

    # -----Setter opp lastvektor-----
    b = lastvektor(fim, fisk, npunkt, punkt, nelem, elem)
    #print(len(b))
    #print(b)

    # ------Setter opp systemstivhetsmatrisen-----
    K = globalStivhetsmatrise(npunkt, punkt, nelem, elem, geometri)
    #print(len(K))
    #print(K)

    # ------Innfører randbetingelser------
    Kn, Bn = bc(npunkt, punkt, K, b)
    #print(len(Kn))
    #print(len(Bn))
    #print(Kn)
    #print(Bn)

    # -----Løser ligningssystemet------
    defo = deformansjon(Kn, Bn)
    #print(len(defo))
    #print(defo)
     
    # -----Hjelp-----
    spen = spennings(punkt, nelem, elem, elementlengder, defo, fim, fisk, ei(nelem, elem, geometri), ei(nelem, elem, geometri))
    #print(len(spen))
    #print(spen)

    #------Finner endemoment for hvert element-----
    endemoment = midtM(spen, nlast, last, npunlast, punlast, nelem, elementlengder)
    #print(len(endemoment))
    #print(endemoment)

    endeskj = midtS(spen, nlast, last, nelem, elementlengder)

    sigma = boyespenning(endemoment, geometri, spen, nelem, elem, ei(nelem, elem, geometri), ei(nelem, elem, geometri))

    maks = maks_sigma(sigma, nelem, elem, geometri)

    #-----Skriver ut hva rotasjonen ble i de forskjellige nodene-----
    #print("Rotasjoner i de ulike punktene:")
    #print(len(rot))

    #-----Skriver ut hva momentene ble for de forskjellige elementene-----
    #print("Elementvis endemoment:")
    #print(len(endemoment))
 
    #-----Plott deformert ramme-----
    skalering = 0.00000005
    plot_structure_def(ax_def, punkt, elem, 1, first_index, skalering*endemoment, file)
    plt.show()

main()