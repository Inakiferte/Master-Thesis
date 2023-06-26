import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np
#matplotlib inline
# load data
med=1
energy, dos, idos = np.loadtxt('dos_tot.dat', unpack=True)
# make plot
plt.figure(figsize = (12, 6))
plt.plot(energy, dos, linewidth=0.75, color='red')
#plt.yticks([])
plt.xlabel('Energy(eV)')
plt.ylabel('DOS')
plt.axvline(x=4.9184, linewidth=0.5, color='k',linestyle=(0, (8, 10)))
plt.xlim(-7.5, 8)
plt.ylim(0,)
plt.fill_between(energy, 0, dos, where=(energy < 4.9184),facecolor='red', alpha=0.25)
plt.text(4.9184, 8, 'Fermi energy', fontsize=med, rotation=90)
plt.show()
