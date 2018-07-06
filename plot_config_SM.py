#!/usr/bin/env python

import sys

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from physics_functions import *

r = np.arange(0.001, 1.5 , 0.01)

#y_1 = V_f_p( r, m_f )
#y_1 = V_ap_q(r) + V_ap_l(r)
y_SM_q = V_SM_q(r)
y_SM_l = V_SM_l(r)
y_SM_f = y_SM_q + y_SM_l
y_SM_v = V_SM_v(r)
y_SM_h = V_SM_h(r)
y = y_SM_f + y_SM_h + y_SM_v

fig, ax = plt.subplots()
ax.plot(r, y,      'k',   label="Total SM",       color='black' )
#ax.plot(r, y_SM_f, 'k--', label="SM fermions", color='red' )
ax.plot(r, y_SM_q, 'k:',  label="SM quarks",   color='maroon' )
ax.plot(r, y_SM_l, 'k:',  label="SM leptons",  color='blue' )
ax.plot(r, y_SM_h, 'k--', label="SM Higgs",    color='green' )
ax.plot(r, y_SM_v, 'k--', label="SM vector bosons", color='orange' )

ax.set(xlabel='$r_c$', ylabel='$V(r_c)$', title='Casimir Potential (SM only)' )
ax.grid()
plt.ylim(-10., 10. )
#plt.ylim( -0.00015, 0.00015 )
legend = ax.legend(loc="upper right", fontsize="medium")

fig.savefig("img/fig_SM.png" )

#plt.show()
