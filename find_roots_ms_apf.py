#!/usr/bin/env python

import sys, os
import subprocess

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as optimize
import scipy.misc     as misc

#from ROOT import *

from physics_functions import *

###################


def V_tot(par):
  r   = par[0]

  m_s = par[1]
  m_f = par[2]
  w_s = par[3]
  w_f = par[4]

  y_SM = V_SM( r )

  y_f  = V_f_m( r, m_f )
  y_s  = V_s_p( r, m_s )

  y = y_SM + w_f*y_f + w_s*y_s

  return y

###################

def find_n_roots( y, r ):
  
  n = len( y )
  
  x0 = []
  for k in xrange(n-1):
    if y[k]*y[k+1] < 0.:     
      x0 += [ r[k] ] 

  return x0

###################

r = np.arange(0.01, 1.5 , 0.01)
  
fig, ax = plt.subplots()

#m_s_range = np.arange( 0.00, 10., 0.1 )
#m_f_range = np.arange( 0.00, 10., 0.1 )
#range_0_1  = np.arange( 0.01, 0.1, 0.01 )
#range_1_10 = np.arange( 1., 10.,  1.)
#range_0_10 = np.concatenate( (range_0_1, range_1_10) )
#m_s_range = range_0_10
#m_f_range = range_0_10
w_s_range = np.arange( 0.5, 20., 0.5 )
w_f_range = np.arange( 0.5, 20., 0.5 )

n_w_s = len(w_s_range)
n_w_f = len(w_f_range)

m_s = 1.8
if len(sys.argv) > 1: m_s = float(sys.argv[1])

m_f = 1.1
if len(sys.argv) > 2: m_f = float(sys.argv[2])

i = 0

#print "INFO: scanning (m_s, m_f) = ( %.2f, %.2f )" % ( m_s, m_f )
for w_s in w_s_range:
  for w_f in w_f_range:
        params = [ r, m_s, m_f, w_s, w_f ]
        y = V_tot( params )
        dy = np.gradient( y )

        y_roots = find_n_roots( dy, r )
        n_roots = len( y_roots )

        if n_roots < 2: continue
        if y[0] < 0.: continue

        print "%.2f, %.2f, %.2f, %.2f, %.2f" % ( m_s, m_f, w_s, w_f, y_roots[0] )

        #c = float(i+1) / float(n)
        #ax.plot( r, y, color="%.2f"%c )
        #i+=1
        ax.plot( r, y )

        cmd = "./plot_config_2.py %.2f %.2f %.2f %.2f" % ( m_s, m_f, w_s, w_f )
        os.system( cmd )

#  print y
ax.set(xlabel='radius', ylabel='Potential', title='Test' )
ax.grid()
plt.ylim(-5, 5 )

s_m = "ms%.1f_mf%.2f_ws%.2f_wf%.2f" % ( m_s, m_f, w_s, w_f )
s_m = s_m.replace(".","p")
fig.savefig("img/derivative_model_ms_apf_%s.png" % s_m)
