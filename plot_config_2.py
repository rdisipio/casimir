#!/usr/bin/env python

import sys

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from physics_functions import *

m_s = 1.8
if len(sys.argv) > 1: m_s = float(sys.argv[1])

m_f = 1.1
if len(sys.argv) > 2: m_f = float(sys.argv[2])

w_s = 1.
if len(sys.argv) > 3: w_s = float(sys.argv[3])

w_f = 1.
if len(sys.argv) > 4: w_f = float(sys.argv[4])

r = np.arange(0.001, 2.0 , 0.01)

y_SM_q = V_SM_q(r)
y_SM_l = V_SM_l(r)
y_SM_f = y_SM_q + y_SM_l
y_SM_v = V_SM_v(r)
y_SM_h = V_SM_h(r)
y_SM = y_SM_f + y_SM_h + y_SM_v

y_f = w_f * V_f_m( r, m_f )
y_s = w_s * V_s_p( r, m_s )
#y_3 = V_s_p( r, m_s )
#y_0 = V_s_massless(r)

y = y_SM + y_f + y_s


fig, ax = plt.subplots()
ax.plot(r, y,   'k',   label="Total",       color='black' )
ax.plot(r, y_SM_f, 'k--', label="SM fermions", color='red' )
#ax.plot(r, y_SM_q, 'k:',  label="SM quarks",   color='maroon' )
#ax.plot(r, y_SM_l, 'k:',  label="SM leptons",  color='cyan' )
ax.plot(r, y_SM_h, 'k--', label="SM Higgs",    color='green' )
ax.plot(r, y_SM_v, 'k--', label="SM vector bosons", color='orange' )
ax.plot(r, y_SM,   'k',   label="Total SM",    color='gray' )
ax.plot(r, y_f,    'k:',  label="$V^-$ fermion (%.1f GeV, $\chi_f$ = %.1f)" % (m_f*m_0, w_f), color='blue' )
ax.plot(r, y_s,    'k-.', label="$V^+$ scalar  (%.1f GeV, $\chi_s$ = %.1f)" % (m_s*m_0, w_s), color='magenta' ) 

ax.set(xlabel='$r_c$', ylabel='$V(r_c)$', title='SM + massive scalar + antiperiodic fermion' )

ax.grid()
plt.ylim(-15., 20. )
legend = ax.legend(loc="upper right", fontsize="medium")

s_m = "ms%.1f_mf%.2f_ws%.2f_wf%.2f" % ( m_s, m_f, w_s, w_f )
s_m = s_m.replace(".","p")
fig.savefig("img/fig_%s.png" % s_m)

#plt.show()
