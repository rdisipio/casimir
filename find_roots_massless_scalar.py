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

  chi = par[1]

#  m_s = par[1]
#  m_f = par[2]
#  w_s = par[3]
#  w_f = par[4]

  y_SM = Calc_SM(r)

#  y_f  = V_f_m(r, m_f )
  #y_s  = V_s_p( r, m_s )
  y_0 = V_s_massless(r)

#  y = y_SM + w_f*y_f + w_s*y_s
  y = y_SM + chi*y_0

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
chi_range = np.arange( 0.0, 150., 10 )
n = len(chi_range)
i = 0
for chi in chi_range:
  params = [ r, chi ]
  y = V_tot( params )
  y = np.gradient( y )

  y_roots = find_n_roots( y, r )
  n_roots = len( y_roots )

  if n_roots == 0: continue

  print chi, y_roots
  
  c = float(i+1) / float(n)
  ax.plot( r, y, color="%.2f"%c )

  i+=1

#  print y
ax.set(xlabel='radius', ylabel='Potential', title='Test' )
ax.grid()
plt.ylim(-.5, .5 )

fig.savefig("img/derivative.png")


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
