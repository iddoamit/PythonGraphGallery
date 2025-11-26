import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
  
palatine = np.array([[104, 36, 109]], dtype=float)
white = np.array([[255, 255, 255]], dtype=float)
diff = (white - palatine)/5

colour = np.concatenate((palatine, palatine+diff, palatine+2*diff, palatine+3*diff), 0)
colour = colour/256

x = np.array([1, 2, 3, 4], dtype=float)
data = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]], dtype=float)

#plt.ion()
#plt.show()

font = {'family': 'Arial', 
        'size': 10, 
        'color': palatine}
        
mpl.rcParams['font.sans-serif'] = "Arial"
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.size'] = 10

fig = plt.figure(figsize=(6, 4), facecolor=(1, 1, 1))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_xlim([0, 4.5])


sep = .05
width = (1-5*sep)/5

B1 = ax.bar(x-(2*width+1.5*sep), data[0, :], width=width, align='edge', color=colour[-1, :], label='2019')
B2 = ax.bar(x-(width+0.5*sep), data[1, :], width=width, align='edge', color=colour[-2, :], label='2020')
B3 = ax.bar(x+0.5*sep, data[2, :], width=width, align='edge', color=colour[-3, :], label='2021')
B4 = ax.bar(x+(width+1.5*sep), data[3, :], width=width, align='edge', color=colour[-4, :], label='2022')

ax.set_xticks(np.linspace(1, 4, 4))
txt = ax.get_xticklabels()
labels = ['Cat. 1', 'Cat. 2', 'Cat. 3', 'Cat. 4']
for k in range(4):
    txt[k].set_text(labels[k])
ax.set_xticklabels(txt)

Leg = ax.legend(frameon=False)

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(1.5)
    
plt.savefig('D:\\Useful Scripts\\Graph Gallery\\Bars\\Bar.pdf', dpi=300)
plt.savefig('D:\\Useful Scripts\\Graph Gallery\\Bars\\Bar.png', dpi=300)

plt.show()