import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import os

here = os.path.dirname(os.path.realpath(__file__))+'\\'

dataset_1 = pd.read_excel(here+'Data.xlsx', sheet_name='Temp', header=0).to_numpy()
dataset_2 = pd.read_excel(here+'Data.xlsx', sheet_name='pn', header=0).to_numpy()

tf = lambda x: 1.8*x+32
tr = lambda x: (x-32)/1.8

ef = lambda x: x*1.6
er = lambda x: x/1.6

aspect = 0.5
fs = 12
figsize = np.array([fs, fs*aspect], dtype=float)
figsize_inch = list(figsize/2.54)
mpl.rcParams['figure.figsize'] = figsize_inch
mpl.rcParams['figure.dpi'] = 300.0
mpl.rcParams['axes.linewidth'] = 1
mpl.rcParams['axes.labelpad'] = 1
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'Arial'
mpl.rcParams['font.size'] = 8
mpl.rcParams['axes.labelpad'] = 6.0
mpl.rcParams['figure.facecolor'] = (1, 1, 1, 1)
mpl.rcParams['axes.facecolor'] = (1, 1, 1, 1)
mpl.rcParams['axes.edgecolor'] = (0, 0, 0, 1)
mpl.rcParams['axes.labelcolor'] = (0, 0, 0, 1)
mpl.rcParams['xtick.color'] = (0, 0, 0, 1)
mpl.rcParams['ytick.color'] = (0, 0, 0, 1)

fig = plt.figure()
ps = 3.65
panelsize_cm = [ps, ps]
panelsize = [panelsize_cm[0]/figsize[0], panelsize_cm[1]/figsize[1]]
hpad = (1-panelsize[0]*2)/3
vpad = (1-panelsize[1])/2

ax1 = fig.add_axes([hpad, vpad, panelsize[0], panelsize[1]])
ax2 = fig.add_axes([hpad*2+panelsize[0], vpad, panelsize[0], panelsize[1]])

ax1.plot(dataset_1[:, 0], 1e3*dataset_1[:, 3], linewidth=1, color=[0.8, 0, 0])
ax2.plot(dataset_2[:, 1], dataset_2[:, 4], linewidth=1, color=[0.8, 0, 0])

ax1_2 = ax1.secondary_xaxis('top', functions=(tf, tr))
ax1.set_xlabel('Temperature (C)')
ax1_2.set_xlabel('Temperature (F)')
ax1.set_xticks(np.linspace(0, 300, 7))
ax1_2.set_xticks(np.linspace(50, 550, 6))
ax1.set_ylabel('Heat Flow (mW)')

ax2_2 = ax2.secondary_yaxis('right', functions=(ef, er))
ax2.set_xscale('log')
ax2.set_xlabel(r'Doping (cm$^{-3}$)')
ax2.set_ylabel('Energy (eV)')
ax2_2.set_ylabel(r'Energy ($\times 10^{-19}$ J)')
ax2.set_xticks([1e14, 1e15, 1e16, 1e17, 1e18, 1e19])
#ax2.set_yticks([0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1])

plt.savefig(here+'DoubleAxis.pdf')
plt.savefig(here+'DoubleAxis.png')

plt.show()