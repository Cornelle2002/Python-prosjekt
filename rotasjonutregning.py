import numpy as np
from numpy.linalg import inv
from randbetingelser import *

def rotasjonsvektor(Kn, Bn):
    Kn_inv = np.linalg.pinv(Kn)
    rot = Kn_inv @ Bn 

    return rot 

def rotasjonsvektor2(Kn, Bn, npunkt):
    Kn_inv = np.linalg.pinv(Kn)
    rot = Kn_inv @ Bn
    rot2 = np.zeros([npunkt])
    for i in range(npunkt):
        rot2[i] = (rot[i * 3 + 2])
    
    return rot2