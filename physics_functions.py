import scipy
from scipy import special
from math import pow, cos
import numpy as np

Kv   = special.kv
Zeta = special.zeta
from scipy import pi

GeV = 1.
MeV = 1e-3

m_0 = 125.0*GeV
#m_0 = 91.2*GeV
#m_0 = 1.

#m_e   =    0.000511*GeV / m_0
#m_mu  =  0.106*GeV     / m_0
#m_tau = 1.78*GeV     / m_0
#m_nu_e = 1e-14
#m_nu_mu  = 1e-14
#m_nu_tau = 1e-14
#m_u   =   0.003*GeV   / m_0
#m_d   =   0.006*GeV   / m_0
#m_s   =   0.1*GeV     / m_0
#m_c   =   1.3*GeV     / m_0
#m_b   =   5.0*GeV   / m_0
#m_t   = 173.3*GeV    / m_0
#m_W   =  80.4*GeV    / m_0
#m_Z   =  91.2*GeV    / m_0
#m_H   = 125.0*GeV    / m_0
#m_gamma = 1e-14

# arXiv:0810.1096 Tab.1
m_e   = 5.6e-6
m_mu  = 1.2e-3
m_tau = 2.0e-2
m_nu_e   = 1e-14
m_nu_mu  = 1e-14
m_nu_tau = 1e-14
m_u = 3.3e-5
m_d = 6.6e-5
m_s = 1.1e-2
m_c = 1.4e-2
m_b = 4.7e-2
m_t = 1.9
m_H = 1.37 # 125 GeV, measured
##m_H = 1.64 # 150 GeV, paper
m_W = 0.88
m_Z = 1.0
m_gamma = 1e-14

####################

def M( n, kR=20. ):
  # see: https://arxiv.org/pdf/0704.3626.pdf
  k = 1e19 # ~ M_pl

  # eq. 2.7 of arXiv:0810.1096
  K = pi * k * exp( -pi*kR )

  return K*(N+0.25)

#~~~~~~~~~~~~~

def V_s_p( r, M=1.0, n=10 ):

    d = 5./2.

    y = -Zeta(d) * pow(M,d) / (32.*pi*pi)
    y *= np.power( r, -d )

    s = 0.
    for i in range(1, n+1):
       s += Kv( d, 2*M*r*i )
    y *= s

    return y

#~~~~~~~~~~~~~

def V_s_m( r, M, n=10 ):
    d = 5./2.

    y = -Zeta(d) * pow(M,d) / (32.*pi*pi)
    y *= np.power( r, -d )

    s = 0.
    for i in range(1, n+1):
        s += Kv( d, 2*M*r*i )*cos(i*pi)
    y *= s

    return y

#~~~~~~~~~~~~~

def V_s_massless(r):
    y = -3.*Zeta(5) / ( 64*pi*pi)
    y *= np.power(r, -4)
    return y

#~~~~~~~~~~~~~

def V_f_p( r, M ):
    return -4.*V_s_p(r,M)

#~~~~~~~~~~~~~

def V_f_m( r, M ):
    return (15./4.)*V_s_p(r,M)

#~~~~~~~~~~~~~

def V_h( r, M=m_H ):
  return 2.*V_s_p(r,M)
  #return V_s_p(r,M)

#~~~~~~~~~~~~~

def V_v( r, M ):
    return 3.*V_s_p(r,M)

#~~~~~~~~~~~~~

def V_lv( r, M ):
    pass

#~~~~~~~~~~~~~

def V_SM_q( r ):
    # SM quarks
    y = 0.

    y += V_f_p( r, m_u )
    y += V_f_p( r, m_d )
    y += V_f_p( r, m_s )
    y += V_f_p( r, m_c )
    y += V_f_p( r, m_b )
    y += V_f_p( r, m_t )

  #  # anti-particles:
  #  y *= 2.
  
    return y

def V_SM_l( r ):
    # SM leptons
    y = 0.
    y += V_f_p( r, m_e )
    y += V_f_p( r, m_mu )
    y += V_f_p( r, m_tau )

 #   # anti-particles:
 #   y *= 2.

    y += V_f_p( r, m_nu_e )
    y += V_f_p( r, m_nu_mu )
    y += V_f_p( r, m_nu_tau )

    return y

def V_SM_v( r ):
    # SM vector bosons
    y = 0.

    y += V_v( r, m_gamma )
    y += V_v( r, m_W )
    y += V_v( r, m_Z )

    return y

  
def V_ap_q(r):
  y = 0.

  y += V_f_m( r, m_u )
  y += V_f_m( r, m_d )
  y += V_f_m( r, m_s )
  y += V_f_m( r, m_c )
  y += V_f_m( r, m_b )
  y += V_f_m( r, m_t )

  # anti-particles:
  y *= 2.
  
  return y

def V_ap_l(r):
  y = 0.
  
  y += V_f_m( r, m_e )
  y += V_f_m( r, m_mu )
  y += V_f_m( r, m_tau )
  
  y += V_f_m( r, m_nu_e )
  y += V_f_m( r, m_nu_mu )
  y += V_f_m( r, m_nu_tau )

  return y
