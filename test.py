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

r = np.arange(0.001, 1.5 , 0.01)

#y_1 = V_f_p( r, m_f )
#y_1 = V_ap_q(r) + V_ap_l(r)
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
#y = np.gradient(y_SM)
#print y

fig, ax = plt.subplots()
ax.plot(r, y,   'k',   label="Total",       color='black' )
ax.plot(r, y_SM_f, 'k--', label="SM fermions", color='red' )
ax.plot(r, y_SM_q, 'k:',  label="SM quarks",   color='maroon' )
ax.plot(r, y_SM_l, 'k:',  label="SM leptons",  color='gold' )
ax.plot(r, y_SM_h, 'k--', label="SM Higgs",    color='green' )
ax.plot(r, y_SM_v, 'k--', label="SM vector bosons", color='orange' )
ax.plot(r, y_SM, 'k',  label="Total SM",    color='gray' )
ax.plot(r, y_f, 'k:',  label="Massive a-p fermion w=%.1f m=%.2f" %(w_f, m_f), color='blue' )
ax.plot(r, y_s, 'k-.', label="Massive scalar      w=%.1f m=%.2f" %(w_s, m_s), color='magenta' )
#ax.plot(r, y_0, 'k-.', label="$V^+_0$ massless scalar ($\chi=$%.0f)" % chi, color='pink' )

ax.set(xlabel='radius', ylabel='Potential', title='Test' )
ax.grid()
plt.ylim(-10., 10. )
#plt.ylim( -0.00015, 0.00015 )
legend = ax.legend(loc="upper right", fontsize="medium")

s_m = "ms%.1f_mf%.2f_ws%.2f_wf%.2f" % ( m_s, m_f, w_s, w_f )
s_m = s_m.replace(".","p")
fig.savefig("img/fig_%s.png" % s_m)

#plt.show()
