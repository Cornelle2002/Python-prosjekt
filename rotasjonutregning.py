import numpy as np
from numpy.linalg import inv
from randbetingelser import *

def rotasjonsvektor(Kn, Bn):
    Kn_inv = np.linalg.pinv(Kn)
    rot = Kn_inv @ Bn 

    return rot 