from structure_visualization import *
from Leseinn import *
 
# -----Rammeanalyse-----
def main():
    # -----Initialiserer figurer-----
    fig_init, ax_init, fig_def, ax_def = setup_plots()
     
    # -----Til visualiseringen, velg første indeks brukt i nummerering av noder og element-----
    # Endre gjerne selv
    first_index = 0
 
    # -----Leser input-data-----
    k, e, f_l, p, nk, ne, nf_l, np= input('input.txt')
 
    #Kaller funksjonen og lagrer oppdatert resultat med riktig verdier                           
    knutepunkt = float_char(k)
    elementer = e
    fordelte_laster = float_char(f_l) 
    punktlaster = float_char(p)


    #Printer for gøy
    print('Antall Knutepunkt: ')
    print(nk)

    print('\n')
    print('Knutepunkt: ')
    for rows in knutepunkt:
        print(rows)

    print('\n')
    print('Antall Elementer: ')
    print(ne)

    print('\n')
    print('Elementer: ')
    for rows in elementer:
        print(rows)

    print('\n')
    print('Antall Fordelte laster: ')
    print(nf_l)

    print('\n')
    print('Fordelte laster: ')
    for rows in fordelte_laster:
        print(rows)

    print('\n')
    print('Antall Punktlast: ')
    print(np)

    print('\n')
    print('Punktlast: ')
    for rows in punktlaster:
        print(rows)

    # -----Plott initalramme-----
    plot_structure(ax_init, knutepunkt, elementer, 1, first_index)
 
    # -----Regner ut lengder til elementene------
    #elementlengder = lengder(knutepunkt, elementer, ne)
 
    # -----Fastinnspenningsmomentene------
    # Lag funksjonen selv
    #fim = moment(npunkt, punkt, nelem, elem, nlast, last, elementlengder)
 
    # -----Setter opp lastvektor-----
    # Lag funksjonen selv
    #b = lastvektor(fim, npunkt, punkt, nelem, elem)
 
    # ------Setter opp systemstivhetsmatrisen-----
    # Lag funksjonen selv
    #K = stivhet(nelem, elem, elementlengder, npunkt)
 
    # ------Innfører randbetingelser------
    # Lag funksjonen selv
    #Kn, Bn = bc(npunkt, punkt, K, b)
 
    # -----Løser ligningssystemet------
    # Lag funksjonen selv
    #rot = ...
    # Hint, se side for løsing av lineære systemer i Python
     
    #------Finner endemoment for hvert element-----
    # Lag funksjonen selv
    #endemoment = endeM(npunkt, punkt, nelem, elem, elementlengder, rot, fim)
 
    #-----Skriver ut hva rotasjonen ble i de forskjellige nodene-----
    #print("Rotasjoner i de ulike punktene:")
    #print(rot)
 
    #-----Skriver ut hva momentene ble for de forskjellige elementene-----
    #print("Elementvis endemoment:")
    #print(endemoment)
 
    #-----Plott deformert ramme-----
    skalering = 100;     # Du kan endre denne konstanten for å skalere de synlige deformasjonene til rammen
    rot = 1
    plot_structure_def(ax_def, knutepunkt, elementer, 1, first_index, skalering*rot)
    plt.show()

main()