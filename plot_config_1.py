#!/usr/bin/env python

import os, sys

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from physics_functions import *

chi = 1.0
if len(sys.argv) > 1: chi = float( sys.argv[1] )

r = np.arange(0.1, 1.5, 0.01)

#y_SM  = V_SM( r )
y_SM_q = V_SM_q(r)
y_SM_l = V_SM_l(r)
y_SM_v = V_SM_v(r)
y_SM_h = V_SM_h(r)
y_SM   = y_SM_q + y_SM_l + y_SM_v + y_SM_h
y_1    = V_s_massless( r )

y = y_SM + chi*y_1

fig, ax = plt.subplots()
ax.plot(r, y, 'k', label="Total", color="black")
ax.plot(r, y_SM_q, 'k--', label="SM quarks", color='red' )
ax.plot(r, y_SM_l, 'k--', label="SM leptons", color='cyan')
ax.plot(r, y_SM_v, 'k--', label="SM vector bosons", color="orange")
ax.plot(r, y_SM_h, 'k--', label="SM Higgs", color="green" )
ax.plot(r, y_1,    'k:',  label="Massless scalar, $\chi$=%.1f"%chi, color="gray" )

#ax.plot(r, y_f_m_light, 'k:', label="Anti-periodic fermion", color="blue")
#ax.plot(r, y_f_m_heavy, 'k:', label="Anti-periodic high-mass fermion", color="blue")

ax.set(xlabel='$r_c$', ylabel='$V(r_c)$', title='SM + massless scalar' )
ax.grid()
plt.ylim(-10, 10 )
legend = ax.legend(loc="upper right", fontsize="medium")

s_chi = "chi%.2f" % chi
s_chi = s_chi.replace(".","p")
fig.savefig("img/fig_massless_scalar_%s.png" % s_chi )

#plt.show()
