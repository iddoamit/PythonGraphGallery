#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 09:11:07 2025

@author: iddoamit_lab
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#Conversion functions:
    #(a) From Miles/kWh to kWh/100 km:
F = lambda x: 100/(x*1.609)
    #(b) From kWh/100 km to Miles/kWh:
G = lambda x: 1/(x/100)/1.609

#Setting the range
miles_extremum = (1, G(10))
miles = np.arange(miles_extremum[0], miles_extremum[1]+1)

#Plot parameters
mpl.rcParams['figure.figsize'] = list(np.array([2.7, 12.])/2.54)
mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['axes.facecolor'] = (0, 0, 0)
mpl.rcParams['axes.linewidth'] = 1
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'Helvetica'
mpl.rcParams['font.size'] = 10

#Plot
fig, ax_mile = plt.subplots()
ax_mile.set_position([0.475, 0.1, 0.05, 0.88])
ax_mile.set_ylim(miles_extremum)
ax_mile.set_xticks([])
ax_mile.set_yticks(np.arange(1, 6.1, 0.5))

ax_km = ax_mile.secondary_yaxis('right', functions=(F, G))
ax_mile.set_ylabel("mi / kWh")
ax_km.set_yticks(np.hstack((np.arange(10, 20, 2), np.arange(20, 31, 5), np.arange(30, 61, 10))))
ax_km.set_ylabel("kWh / 100 km")

plt.show()