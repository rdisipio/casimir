# casimir
Casimir potential 5D radius compactification.


Make plots
==========

You need the following software packages to be installed:

```
python     - 2.7.14
numpy      - 0.14.3
scipy      - 1.1.0
matplotlib - 2.2.2
```

Create a directory to save the plots:
```mkdir -p img```

Plot potential for Standard Model only:
```
./plot_config_SM.py
```

Plot potential for SM + massless scalar + LV vector
```
./plot_config_1.py $chi
```

where ```$chi``` is the strength of the coupling to the LV vector

Plot potential for SM + antiperiodic fermion + massive scalar
```
./plot_config_2.py $ms $mf $chi_ms $chi_mf
```

where ```$ms```, ```$mf```, ```$chi_ms``` and ```$chi_mf``` are the mass of the scalar, the mass of the fermion and the 
coupling to the LV vector(s) to the scalar and to the fermion respectively

Parameters scan
===============

Make sure you have GNU-parallel installed in the system.

Scan the coupling parameter for the massless scalar:
```seq 0.0 10 200 | parallel ./plot_config_1.py {}```

Scan the coupling parameters for given masses of the scalar and of the antiperiodic fermion:

```./search_ms_afp.sh $ms $mf```

