import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import curve_fit

## Generate data

def H(x, a0, a1, tau):
    return a0+a1*np.exp(-x/tau)

t = np.linspace(0, 1e-3, 256)
data = np.zeros((256, 6), dtype=float)
A0 = np.linspace(1e-9, 3e-9, 6)
A1 = np.linspace(1e-10, 3e-10, 6)
tau = 3e-4
for h in range(256):
    for k in range(6):
        data[h, k] = A0[k] - (A0[k]-A1[k])*np.exp(-t[h]/tau)
noise = np.random.uniform(-1e-10, 1e-10, data.shape)

data = data + noise

fits = np.zeros_like(data)
A1_vec = np.zeros(6)

for k in range(6):
    f, g = curve_fit(H, t, data[:, k], p0=(data[-1, k], -data[-1, k], 1e-4))
    fits[:, k] = f[0] + f[1]*np.exp(-t/f[2])
    A1_vec[k] = -f[1]
    
Bias = np.linspace(0.2, 1.2, 6)
PF = np.polyfit(Bias, A1_vec, 1)

## End of data generation

font = {'family': 'Arial', 
        'size': 8, 
        'color': 'black'}
        
mpl.rcParams['font.sans-serif'] = "Arial"
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.size'] = 10

colour = np.array([[0, 0, 0], # black
                   [0.8, 0, 0], # red
                   [0, 0, 0.8], # blue
                   [0, 0.5, 0], # green
                   [0.45, 0, 0.45], # purple
                   [0.8, 0.4, 0]], dtype=float) # orange
                   
fig = plt.figure(figsize=(5, 5), facecolor=(1, 1, 1))
ax0 = fig.add_axes([0.12, 0.12, 0.8, 0.8])
ax1 = fig.add_axes([0.12, 0.75, 0.3, 0.17]) # optional inset

ax0.set_xlabel('Time (ms)')
ax0.set_ylabel('Current (nA)')

alpha = 0.2
S0 = ax0.scatter(1e3*t, 1e9*data[:, 0], marker='o', edgecolors=np.concatenate((colour[0, :], np.array([alpha], dtype=float))), facecolor=(1, 1, 1, 0), s=20)
S1 = ax0.scatter(1e3*t, 1e9*data[:, 1], marker='o', edgecolors=np.concatenate((colour[1, :], np.array([alpha], dtype=float))), facecolor=(1, 1, 1, 0), s=20)
S2 = ax0.scatter(1e3*t, 1e9*data[:, 2], marker='o', edgecolors=np.concatenate((colour[2, :], np.array([alpha], dtype=float))), facecolor=(1, 1, 1, 0), s=20)
S3 = ax0.scatter(1e3*t, 1e9*data[:, 3], marker='o', edgecolors=np.concatenate((colour[3, :], np.array([alpha], dtype=float))), facecolor=(1, 1, 1, 0), s=20)
S4 = ax0.scatter(1e3*t, 1e9*data[:, 4], marker='o', edgecolors=np.concatenate((colour[4, :], np.array([alpha], dtype=float))), facecolor=(1, 1, 1, 0), s=20)
S5 = ax0.scatter(1e3*t, 1e9*data[:, 5], marker='o', edgecolors=np.concatenate((colour[5, :], np.array([alpha], dtype=float))), facecolor=(1, 1, 1, 0), s=20)
P0, = ax0.plot(1e3*t, 1e9*fits[:, 0], color=colour[0, :], linewidth=1.5, label=r'V$_{ds}$ = 0.2 V')
P1, = ax0.plot(1e3*t, 1e9*fits[:, 1], color=colour[1, :], linewidth=1.5, label=r'V$_{ds}$ = 0.4 V')
P2, = ax0.plot(1e3*t, 1e9*fits[:, 2], color=colour[2, :], linewidth=1.5, label=r'V$_{ds}$ = 0.6 V')
P3, = ax0.plot(1e3*t, 1e9*fits[:, 3], color=colour[3, :], linewidth=1.5, label=r'V$_{ds}$ = 0.8 V')
P4, = ax0.plot(1e3*t, 1e9*fits[:, 4], color=colour[4, :], linewidth=1.5, label=r'V$_{ds}$ = 1.0 V')
P5, = ax0.plot(1e3*t, 1e9*fits[:, 5], color=colour[5, :], linewidth=1.5, label=r'V$_{ds}$ = 1.2 V')

Leg = ax0.legend(frameon=False, loc='lower right', ncols=2)

## Optional inset
ax1.yaxis.tick_right()
ax1.yaxis.set_label_position('right')
ax1.set_xlabel('Bias (V)', fontdict=font)
ax1.set_ylabel(r'A$_{1}$ (nA)', fontdict=font)
ax1.yaxis.set_ticklabels(ax1.yaxis.get_ticklabels(), fontdict=font)
ax1.xaxis.set_ticklabels(ax1.xaxis.get_ticklabels(), fontdict=font)

F1 = ax1.plot(Bias, 1e9*np.polyval(PF, Bias), color=(0, 0, 0, 1), linestyle='--', linewidth=2)
F0 = ax1.scatter(Bias, 1e9*A1_vec, marker='o', edgecolors=(1, 1, 1, 0), facecolor=(1, 0, 0, 1), s=50)

# End optional inset
for axis in ['top', 'bottom', 'left', 'right']:
    ax0.spines[axis].set_linewidth(1.5)
    ax1.spines[axis].set_linewidth(1.5) # optional inset

plt.savefig('D:\\Useful Scripts\\Graph Gallery\\Scatter and Fit\\Scatter and Fit.pdf', dpi=300)
plt.savefig('D:\\Useful Scripts\\Graph Gallery\\Scatter and Fit\\Scatter and Fit.png', dpi=300)

plt.show()