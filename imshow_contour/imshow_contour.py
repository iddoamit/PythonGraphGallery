import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import os

here = os.path.dirname(os.path.realpath(__file__))+'\\' 

def fmt(x):
    if x<1e-4:
        return f'{x*1e7:.0f}'+' nm'
    else:
        return f'{x*1e4:.0f}'+r' $\mu$m'

q = 1.6e-19
e0 = 8.85e-14
er = 11.7
n = np.linspace(14, 19, 200)
N = 10**n
k = 8.6e-5
T = 300
kT = k*T
ni = 1e10

A = np.sqrt(2*e0*er/q)
X, Y = np.meshgrid(N, N)
B = np.sqrt((X+Y)/(X*Y))
Vbi = kT*np.log(X*Y/(ni**2))
W = A*B*np.sqrt(Vbi)

figsize_cm = np.array([10, 8])
figsize = list(figsize_cm/2.54)

mpl.rcParams['figure.dpi'] = 150
mpl.rcParams['figure.figsize'] = figsize
mpl.rcParams['axes.labelpad'] = 1
mpl.rcParams['axes.linewidth'] = 1
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'Arial'
mpl.rcParams['font.size'] = 8

fig, axs = plt.subplot_mosaic([['a', 'cb']], width_ratios=[1, 0.1], layout='constrained')

axs['a'].set_xlabel('Donor doping (cm'+r'$^{-3}$)')
axs['a'].set_ylabel('Acceptor doping (cm'+r'$^{-3}$)')

I = axs['a'].imshow(W, extent=(n[0], n[-1], n[0], n[-1]), origin='lower', norm=LogNorm(vmin=1e-6, 
                                                                                       vmax=1e-3), 
                    cmap='YlOrBr_r')

C = axs['a'].contour(n, n, W, [1e-6, 2e-6, 5e-6, 1e-5, 2e-5, 5e-5, 1e-4, 2e-4, 5e-4, 1e-3], 
                     linewidths=1)
C.set_edgecolor((0, 0, 0.8, 1))
D = axs['a'].clabel(C, C.levels, inline=True, fmt=fmt, fontsize=7)

CB = plt.colorbar(I, cax=axs['cb'])

BBa = axs['a'].get_position()
BBcb = axs['cb'].get_position()
points_a = BBa.get_points()
points_cb = BBcb.get_points()
points_cb[:, 1] = points_a[:, 1]
BBcb.set_points(points_cb)
axs['a'].set_position(BBa)
axs['cb'].set_position(BBcb)

axs['cb'].set_xlabel('W (cm)')

axs['cb'].xaxis.set_label_coords(.5, -.10)
plt.savefig(here+'imshow_contour.pdf')
#plt.ion()
plt.show()
