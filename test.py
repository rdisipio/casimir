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

chi = m_s

r = np.arange(0.01, 1.5 , 0.01)


#y_f = V_SM_q( r ) + V_SM_l( r )
#y_q = V_SM_q( r )
#y_l = V_SM_l( r )
#y_f = y_q + y_l
#y_f = V_f_p( r, m_t ) + V_f_p( r, m_b )
#y_f = V_f_p( r, m_t )
#y_h = V_h( r )
#y_v = V_SM_v( r )
#y_SM = y_f + y_h #+ y_v

#y_1 = V_f_p( r, m_f )
#y_1 = V_ap_q(r) + V_ap_l(r)
y_f = V_SM_q(r) + V_SM_l(r)
y_v = V_SM_v(r)
y_h = V_h(r)
y_SM = y_f + y_v + y_h
#y_2 = V_s_p( r, m_s )
#y_2 = V_f_m(r, m_f )
#y_3 = V_s_p( r, m_s )
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
#plt.ylim( -0.00015, 0.00015 )
legend = ax.legend(loc="upper right", fontsize="medium")

s_m = "ms%.1f_mf%.2f" % ( m_s, m_f )
s_m = s_m.replace(".","p")
fig.savefig("img/fig_%s.png" % s_m)

#plt.show()
