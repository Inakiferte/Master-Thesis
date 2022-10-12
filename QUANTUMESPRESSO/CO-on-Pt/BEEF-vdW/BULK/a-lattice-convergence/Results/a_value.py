import numpy as np

# ## Konfigurazioak

a = np.loadtxt("a.dat")[:, 0]
Energy = np.loadtxt("a.dat")[:, 1]

for i in range(len(a)-1):
    if Energy[ i + 1 ] < Energy[ i ]:
       a_value = a[ i + 1 ]

print( 'a value: ', a_value)

       
