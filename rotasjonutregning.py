import numpy as np
from numpy.linalg import inv
from randbetingelser import *

def deformansjon(Kn, Bn):
    Kn_inv = np.linalg.pinv(Kn)
    defo = Kn_inv @ Bn

    return defo
