#!/usr/bin/env python

import sys

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from physics_functions import *

chi = 50
if len(sys.argv) > 1: chi = float(sys.argv[1])

r = np.arange(0.01, 1.5 , 0.01)

y_f = V_SM_q(r) + V_SM_l(r)
y_v = V_SM_v(r)
y_h = V_h(r)
y_SM = y_f + y_v + y_h
y_0 = V_s_massless(r)

y = y_SM + chi*y_0

fig, ax = plt.subplots()
ax.plot(r, y,   'k',   label="Total",       color='black' )
ax.plot(r, y_f, 'k--', label="SM fermions", color='red' )
#ax.plot(r, y_q, 'k--', label="SM quarks", color='red' )
#ax.plot(r, y_l, 'k:', label="SM leptons", color='yellow' )
ax.plot(r, y_h, 'k--', label="SM Higgs",    color='green' )
ax.plot(r, y_v, 'k--', label="SM vector bosons", color='orange' )
ax.plot(r, y_SM, 'k',  label="Total SM",    color='gray' )
#ax.plot(r, y_1, 'k:',  label="Massive antiperiodic fermion %.2f" % m_f, color='blue' )
#ax.plot(r, y_2, 'k-.', label="Massive scalar %.1f"%m_s, color='magenta' )
ax.plot(r, y_0, 'k-.', label="$V^+_0$ massless scalar ($\chi=$%.0f)" % chi, color='pink' )

ax.set(xlabel='radius', ylabel='Potential', title='Test' )
ax.grid()
plt.ylim(-10., 10. )
legend = ax.legend(loc="upper right", fontsize="medium")

s_chi = "chi%.1f" % ( chi )
s_chi = s_chi.replace(".","p")
fig.savefig("img/fig5_massless_%s.png" % s_chi)

#plt.show()
