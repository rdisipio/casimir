#!/usr/bin/env python

import sys

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as optimize
import scipy.misc     as misc

#from ROOT import *

from physics_functions import *

###################

def Calc_SM(r):
  y_f = V_SM_q(r) + V_SM_l(r)
  y_v = V_SM_v(r)
  y_h = V_h(r)
  y_SM = y_f + y_h + y_v
  return y_SM

###################

def V_tot(par):
  r   = par[0]

  m_s = par[1]
  m_f = par[2]
  w_s = par[3]
  w_f = par[4]

  y_SM = Calc_SM(r)

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
range_0_1  = np.arange( 0.01, 0.1, 0.01 )
range_1_10 = np.arange( 1., 10.,  1.)
range_0_10 = np.concatenate( (range_0_1, range_1_10) )
m_s_range = range_0_10
m_f_range = range_0_10
w_s_range = np.arange( 0.50, 20., 0.5 )
w_f_range = np.arange( 0.50, 20., 0.5 )

n_m_s = len(m_s_range)
n_m_f = len(m_f_range)
n_w_s = len(w_s_range)
n_w_f = len(w_f_range)

i = 0
for m_s in m_s_range:
  for m_f in m_f_range:
    print "INFO: scanning (m_s, m_f) = ( %.2f, %.2f )" % ( m_s, m_f )
    for w_s in w_s_range:
      for w_f in w_f_range:
        params = [ r, m_s, m_f, w_s, w_f ]
        y = V_tot( params )
        dy = np.gradient( y )

        y_roots = find_n_roots( dy, r )
        n_roots = len( y_roots )

        if n_roots == 0: continue

        print "%.2f, %.2f, %.2f, %.2f, %.2f" % ( m_s, m_f, w_s, w_f, y_roots[0] )
  
        #c = float(i+1) / float(n)
        #ax.plot( r, y, color="%.2f"%c )
        #i+=1
        ax.plot( r, y )

#  print y
ax.set(xlabel='radius', ylabel='Potential', title='Test' )
ax.grid()
plt.ylim(-.5, .5 )

fig.savefig("img/derivative_model2.png")


#initial_guess = [ 0.5, 1.8, 1.1, 1.0, 1.0 ]
#par_range = [
#  [ 0.01, 3.0 ],
#  [ 0.01, 100. ],
#  [ 0.01, 100. ],
#  [ 0.01, 100. ],
#  [ 0.01, 100. ],
#  ]
#result = optimize.minimize( V_tot, initial_guess, bounds=par_range )
#result = optimize.fsolve( V_tot, initial_guess )

#if result.success:
#    print "INFO: Optimization successful"
#    fitted_params = result.x
#    print(fitted_params)
#else:
#    raise ValueError(result.message)
