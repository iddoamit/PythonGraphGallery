"""
Created on Fri May 30 14:22:27 2025

@author: @iddoamit
"""
#Import packages
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import os

#Data import and conversion
path = os.path.dirname(os.path.realpath(__file__))+'/'
filename1 = 'input1.csv'
filename2 = 'input2.csv'

data1 = pd.read_csv(path+filename1, header=0).to_numpy()
data2 = pd.read_csv(path+filename2, header=0).to_numpy()

Q1a = data1[:, 0]
Q2a = data1[:, 1]
Q3a = data1[:, 2]
Q4a = data1[:, 3]
Q1b = data2[:, 0]
Q2b = data2[:, 1]
Q3b = data2[:, 2]
Q4b = data2[:, 3]

TotalMarks_a = (Q1a+Q2a+Q3a+Q4a)/4
TotalMarks_b = (Q1b+Q2b+Q3b+Q4b)/4

x = np.arange(1, 6)

#Figure set up
mpl.rcParams['figure.figsize'] = list(np.array([18., 7.])/2.54)
mpl.rcParams['figure.facecolor'] = (1, 1, 1)
mpl.rcParams['figure.dpi'] = 600
mpl.rcParams['axes.linewidth'] = 1
mpl.rcParams['axes.facecolor'] = mpl.rcParams['figure.facecolor']
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'helvetica'
mpl.rcParams['font.size'] = 9
mpl.rcParams['axes.edgecolor'] = np.array([0, 42, 65])/255
mpl.rcParams['axes.labelcolor'] = np.array([0, 42, 65])/255
mpl.rcParams['xtick.color'] = np.array([0, 42, 65])/255
mpl.rcParams['ytick.color'] = np.array([0, 42, 65])/255

fig, axs = plt.subplots(tight_layout=True)
axs.set_xlabel('Marking Item')
axs.set_ylabel('Marks')

'''
The violin plots are plotted as two series, one plotted with 'low' side, ie., 
the side at negative value to the location mark, and the other on the 'high' side.
'''
VA = axs.violinplot([Q1a, Q2a, Q3a, Q4a, TotalMarks_a], 
                    side='low', showextrema=False, showmeans=True)
VB = axs.violinplot([Q1b, Q2b, Q3b, Q4b, TotalMarks_b], 
                    side='high', showextrema=False, showmeans=True)

#X-Axes labels
axs.set_xticks(np.arange(1, 6))
XTL = axs.get_xticklabels()
for i in range(5):
    if i == 4:
        XTL[i].set_text('Total Marks')
    else:
        XTL[i].set_text(f'Question {i+1:.0f}')
axs.set_xticklabels(XTL)

for body in VA['bodies']:
    body.set_facecolor(np.array([203, 122, 41])/255)
    body.set_alpha(0.7)
VA['cmeans'].set_edgecolor(np.array([203, 122, 41])/255)

for body in VB['bodies']:
    body.set_facecolor(np.array([41, 122, 203])/255)
    body.set_alpha(0.7)
VB['cmeans'].set_edgecolor(np.array([41, 122, 203])/255)

a_label = {'font': 'helvetica', 'size': 9, 'color': np.array([203, 122, 41])/255}
d_label = {'font': 'helvetica', 'size': 9, 'color': np.array([41, 122, 203])/255}

axs.text(0.6, 6, 'Group B', ha='left', va='bottom', fontdict=d_label)
axs.text(0.6, 14, 'Group A', ha='left', va='bottom', fontdict=a_label)

fig.savefig(path+'outcome.pdf')
fig.savefig(path+'outcome.png')

