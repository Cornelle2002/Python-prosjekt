from lesinput import *  
from structure_visualization import *  
from verktøy import *                   
from fastinnspenning import *          
from lastvektor import *             
from tverrsnitt import *      
from EIEA import *               
from matriser import *                             
from globalstivhetsmatrise import *                 
from randbetingelser import *                       
from rotasjon import *
from endekrefter import *
from maxkrafter import *
from plot import *
from flyt import * 
from iterasjon import * 

# -----Rammeanalyse-----
def main():
    # -----Initialiserer figurer-----
    fig_init, ax_init, fig_def, ax_def = setup_plots()
     
    # -----Til visualiseringen, velg første indeks brukt i nummerering av noder og element-----
    first_index = 0
 
    # -----Leser input-data-----
    file = 'input_konstruksjon.txt'
    
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
    EI = ei(nelem, elem, geometri)
    EA = ea(nelem, elem, geometri)

    # -----Fastinnspenningsmomentene------
    r = fastinnspenningskrefter(nelem, elem, nlast, last, npunlast, punlast, geometri, elementlengder)
    
    # -----Setter opp lastvektor-----
    R = lastvektor(r, npunkt, punkt, nelem, elem)
    R1 = punktkrefter(elem, npunkt, punkt, npunlast, punlast, elementlengder)
    tot_R = np.matrix(R1 - R)

    # ------Setter opp systemstivhetsmatrisen-----
    K = globalStivhetsmatrise(npunkt, punkt, nelem, elem, geometri, EI, EA, elementlengder)

    # ------Innfører randbetingelser------
    K = randbetingelser(npunkt, punkt, K)
    
    # -----Løser ligningssystemet------
    L = np.linalg.inv(K)*np.transpose(tot_R)    

    #------Finner endemoment for hvert element-----
    endeK = endekrefter(punkt, nelem, elem, L, r, EI, EA)
    
    #------Finner maxmoment for hvert element-----
    max_m = max_moment(endeK, nelem, elem, nlast, last, npunlast, punlast, elementlengder)
    max_sk = max_skjaer(nelem, endeK)
    max_n = max_aksial(nelem, endeK)

    #------Plotter moment, skjærkraft og normalkraft for hvert element------
    plotting(endeK, nelem, nlast, last, npunlast, punlast, elementlengder)

    #-----Finner flytspenningen for elementene-------
    sigma_ho, sigma_jack, sigma_ver, sigma_k, sigma_i = sigma_flyt(max_m, max_n, nelem, elem, geometri, EI, EA)
    sigma = [sigma_ho, sigma_jack, sigma_ver, sigma_k, sigma_i]
    
    #-----Tverrsnittsdimensjonene etter iterasjon-----
    tverr = iterasjon(sigma, nelem, elem, geometri)
    
    #-----Skriver ut hva rotasjonen ble i de forskjellige nodene-----
    skalering = 50
    rot = rotasjoner(npunkt, L, skalering)
     
    #-----Plott deformert ramme-----
    plot_structure_def(ax_def, punkt, elem, 1, first_index, rot, file)
    plt.show()

main()