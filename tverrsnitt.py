import numpy as np

#Formler for A og I er hentet fra formelsamling i Mekanikk 2

#Andre arealmoment for I-profil
def i_iprofil(h, b, f, s):
    #h - høyde
    #b - bredde
    #f - flenstykkelse
    #s - stegtykkelse

    steg = (s * h**3)/12
    flens = (b * f**3)/12
    tverr = flens + steg + flens 

    return tverr

#Andre arealmoment for Boks-profil
def i_kvadrat(h, b, t):
    #h - ramme lengde
    #b - bredde
    #t - tykkelse

    ytre = (1/12) * b * h**3
    indre = (1/12) * (b-2*t) * (h-2*t)**3
    tverr = ytre - indre

    return tverr

#Andre arealmoment for Rør-profil
def i_ror(d, t):
    #d - diameter ytre
    #t - tykkelse

    tverr = (np.pi * ((d/2)**4 - ((d/2)-t)**4)) / 4

    return tverr

#Areal for I-profil
def a_iprofil(h, b, f, s):
    #h - høyde
    #b - bredde
    #f - flenstykkelse
    #s - stegtykkelse

    steg = h * s
    flens = b * f
    areal = flens + steg + flens

    return areal

#Areal for Boks-profil
def a_kvadrat(h, b, t):
    #h - ramme lengde
    #b - bredde
    #t - tykkelse

    ytre = h * b
    indre = (h - 2*t) * (b - 2*t)
    areal = ytre - indre

    return areal

#Areal for Rør-profil
def a_ror(d, t):
    #d - diameter ytre
    #t - tykkelse

    areal = np.pi * ((d/2)**2 - ((d/2)-t)**2)

    return areal