import numpy as np

def i_iprofil(h, b, f, s):
    #h - høyde
    #b - bredde
    #f - flenstykkelse
    #s - stegtykkelse

    steg = (1/12) * (h-2*f)**3 * s
    flens = (1/12 * f**3 * b +(h/2 - f/2)**2 *f *b) * 2
    tverr = steg + flens
    return tverr

def i_kvadrat(h, b, t):
    #h - ramme lengde
    #t - tykkelse

    ytre = (1/12) * b * h**3
    indre = (1/12) * (b-2*t) * (h-2*t)**3
    tverr = ytre - indre
    return tverr

def i_ror(d, t):
    #d - diameter ytre
    #t - tykkelse

    tverr = (np.pi *((d/2)**4 - ((d/2)-t)**4)) / 4
    return tverr