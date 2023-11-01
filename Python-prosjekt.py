#from tabulate import tabulate

from lesinput import *
from structure_visualization import *
from verktøy import *
from moment import *
from lastvektor import *
from globalstivhetsmatrise import *
from randbetingelser import *
from rotasjonutregning import *
from Endemoment import *
from EIEA import *


 
# -----Rammeanalyse-----
def main():
    # -----Initialiserer figurer-----
    fig_init, ax_init, fig_def, ax_def = setup_plots()
     
    # -----Til visualiseringen, velg første indeks brukt i nummerering av noder og element-----
    first_index = 0
 
    # -----Leser input-data-----
    k, e, f_l, p, g, nk, ne, nf_l, npu= input('input.txt')
 
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
    
    #Printer for gøy

    # -----Plott initalramme-----
    #plot_structure(ax_init, punkt, elem, 1, first_index)

    
    # -----Regner ut lengder til elementene------
    elementlengder = lengder(punkt, elem, nelem)
 
    # -----Fastinnspenningsmomentene------
    fim, fisk = moment(nelem, elem, nlast, last, npunlast, punlast, geometri, elementlengder)
 
    # -----Setter opp lastvektor-----
    b = lastvektor(fim, fisk, npunkt, punkt, nelem, elem)

    # ------Setter opp systemstivhetsmatrisen-----
    K = globalStivhetsmatrise(npunkt, punkt, nelem, elem, geometri)

    for row in K:
        print(row)
 
    # ------Innfører randbetingelser------
    Kn, Bn = bc(npunkt, punkt, K, b)
 
    # -----Løser ligningssystemet------
    rot = rotasjonsvektor(Kn, Bn)


    d = spennings(punkt, nelem, elem, elementlengder, rot, fim, fisk, ei(nelem, elem, geometri), ei(nelem, elem, geometri))


    tes = midtS(d, nlast, last, nelem, elementlengder)

    sigma = boyespenning(tes, geometri, d, nelem, elem, ei(nelem, elem, geometri), ei(nelem, elem, geometri))

    maks = maks_sigma(sigma, nelem, elem, geometri)
     
    #------Finner endemoment for hvert element-----
    endemoment = midtM(d, nlast, last, npunlast, punlast, nelem, elementlengder)

    #-----Skriver ut hva rotasjonen ble i de forskjellige nodene-----
    print("Rotasjoner i de ulike punktene:")
    print(rot)
 
    #-----Skriver ut hva momentene ble for de forskjellige elementene-----
    #print("Elementvis endemoment:")
    #print(endemoment)
 
    #-----Plott deformert ramme-----
    skalering = 0.2;     # Du kan endre denne konstanten for å skalere de synlige deformasjonene til rammen
    plot_structure_def(ax_def, punkt, elem, 1, first_index, skalering*rot)
    plt.show()

main()