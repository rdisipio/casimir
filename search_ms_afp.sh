#!/bin/bash

parallel -a seq_0_05_10.dat -a seq_mf.dat ./find_roots_ms_apf.py

#m_s_min=1.0
#m_s_max=10.

#for m_f in 0.02 0.1 1.1 2. 5. 10.
#do	   
#    seq ${m_s_min} 0.5 ${m_s_max} | parallel ./find_roots_ms_apf.py {} ${m_f}
#done
