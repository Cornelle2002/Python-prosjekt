from lesinput import *

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

 
def setup_plots():
    fig_init, ax_init = plt.subplots()
    fig_def, ax_def = plt.subplots()
    ax_init.set_title('Initialramme')
    ax_def.set_title('Deformert ramme')
    ax_init.axes.set_aspect('equal')
    ax_def.axes.set_aspect('equal')
    return fig_init, ax_init, fig_def, ax_def
 
def plot_structure(ax, punkt, elem, numbers, index_start, file):
    # This is a translation of the original function written by Josef Kiendl in Matlab
    # It has been slightly modified in order to be used in TMR4176
 
    # This function plots the beam structure defined by nodes and elements
    # The bool (0 or 1) 'numbers' decides if node and element numbers are plotted or not
    
    k, e, f_l, p, g, nk, ne, nf_l, npu= input(file)

    punkt = float_char(k)
    elem = float_char(e)

    punkt = np.array(punkt)
    elem = np.array(elem)

    # Change input to the correct format
    nodes = np.array(punkt[:, 0:2], copy = 1, dtype = int)
    el_nod = np.array(elem[:, 0:2], copy=1, dtype=int) + 1
 
    # Start plotting part
    for iel in range(0, el_nod.shape[0]):
        # Plot element
        ax.plot([nodes[el_nod[iel, 0] - 1, 0], nodes[el_nod[iel, 1] - 1, 0]],
                [nodes[el_nod[iel, 0] - 1, 1], nodes[el_nod[iel, 1] - 1, 1]], '-k', linewidth = 2)
 
        if numbers == 1:
            # Plot element numbers. These are not plotted in the midpoint to
            # avoid number superposition when elements cross in the middle
            ax.text(nodes[el_nod[iel, 0] - 1, 0] + ( nodes[el_nod[iel, 1] - 1, 0] - nodes[el_nod[iel, 0] - 1, 0] ) / 2.5,
                    nodes[el_nod[iel, 0] - 1, 1] + ( nodes[el_nod[iel, 1] - 1, 1] - nodes[el_nod[iel, 0] - 1, 1] ) / 2.5,
                    str(iel + index_start), color = 'blue', fontsize = 16)
 
    if numbers == 1:
        # Plot node number
        for inod in range(0, nodes.shape[0]):
            ax.text(nodes[inod, 0], nodes[inod, 1], str(inod + index_start), color = 'red', fontsize = 16)
 
 
def plot_structure_def(ax, punkt, elem, numbers, index_start, r, file):
    # This is a translation of the original function written by Josef Kiendl in Matlab
    # This function plots the deformed beam structure defined by nodes and elements
    # The bool (0 or 1) 'numbers' decides if node and element numbers are plotted or not
 
    k, e, f_l, p, g, nk, ne, nf_l, npu= input(file)

    punkt = float_char(k)
    elem = float_char(e)

    punkt = np.array(punkt)
    elem = np.array(elem)

    # Change input to the correct format
    nodes = np.array(punkt[:, 0:2], copy = 1, dtype = int)
    el_nod = np.array(elem[:, 0:2], copy=1, dtype=int) + 1
    nod_dof = np.arange(0, nodes.shape[0] + 1, 1, dtype=int)
 
    if numbers == 1:
        # Plot node number
        for inod in range(0, nodes.shape[0]):
            ax.text(nodes[inod, 0], nodes[inod, 1], str(inod + index_start), color = 'red', fontsize = 16)
 
    for iel in range(0, el_nod.shape[0]):
        delta_x = nodes[el_nod[iel, 1] - 1, 0] - nodes[el_nod[iel, 0] - 1, 0]
        delta_z = nodes[el_nod[iel, 1] - 1, 1] - nodes[el_nod[iel, 0] - 1, 1]
        L = np.sqrt(delta_x ** 2 + delta_z ** 2)
        if delta_z >= 0:
            psi = np.arccos(delta_x / L)
        else:
            psi = -np.arccos(delta_x / L)
 
        phi = np.zeros((2, 1))
        for inod in range(0, 2):
            if nod_dof[el_nod[iel, inod] - 1] > 0:
                phi[inod] = r[nod_dof[el_nod[iel, inod] - 1] - 1]
        x = np.array([0, L])
        z = np.array([0, 0])
        xx = np.arange(0, 1.01, 0.01)*L
        cs = CubicSpline(x, z, bc_type = ((1, -phi[0, 0]), (1, -phi[1, 0])))
        zz = cs(xx)
 
        # Rotate
        xxzz = np.array([[np.cos(psi), -np.sin(psi)], [np.sin(psi), np.cos(psi)]]) @ np.vstack([xx, zz])
 
        # Displace
        xx2 = xxzz[0, :] + nodes[el_nod[iel, 0] - 1, 0]
        zz2 = xxzz[1, :] + nodes[el_nod[iel, 0] - 1, 1]
        ax.plot(xx2, zz2, '-k', linewidth = 2)
 
        if numbers == 1:
            # Plot element numbers. These are not plotted in the midpoint to
            # avoid number superposition when elements cross in the middle
            ax.text(xx2[round(xx2.size / 2.5)], zz2[round(xx2.size / 2.5)], str(iel + index_start), color = 'blue', fontsize = 16)