"""
Broken axis example, where the x-axis will have a portion cut out.
"""
import matplotlib.pylab as plt
import numpy as np


data_pdos = "/scratch/inakiferte/CO_on_Pt/BEEF-vdW/CO_Top/results_ph_scf1_qgrid6_final/phonon.dos"

with open(data_pdos) as f:
    pdos = np.loadtxt(f,skiprows=0)

freq = pdos[:,0]
totdos = pdos[:,1]
cdos = pdos[:,2]
odos = pdos[:,3]
codos = cdos + odos

fontsize=15

f, (ax, ax2) = plt.subplots(1, 2, sharey=True, facecolor='w',
figsize=(12,6))
f.subplots_adjust(wspace=0.05)
plt.ylim(0,)

ax.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=False, top=True, direction='out')

ax2.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True, top=True, direction='out')

ax.text(570, -0.11, '$\omega~(cm^{-1})$', ha='center', va='bottom', fontsize=fontsize)
ax.text(-170, 0.5, 'F($\omega$)',rotation=90, ha='center', va='bottom', fontsize=fontsize)
ax2.text(2037, 0.15, 'IS', ha='center', va='bottom', fontsize=fontsize)
ax.text(480, 0.45, 'ES', ha='center', va='bottom', fontsize=fontsize)


ax.plot(freq, totdos, color="blue", label="total")
ax.fill_between(freq, totdos, facecolor='blue')
ax2.plot(freq, totdos, color="blue")
ax2.fill_between(freq, totdos,  facecolor='blue', label="total")

ax.plot(freq, codos, color="orange", label="CO")
ax.fill_between(freq, codos, facecolor='orange')
ax2.plot(freq, codos, color="orange")
ax2.fill_between(freq, codos,  facecolor='orange', label="CO")

plt.legend(fontsize=fontsize-2)

ax.set_xlim(freq[0], 550)
ax2.set_xlim(1900, freq[-1])

ax.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.yaxis.tick_right()

d = 0.015
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((1-d, 1+d), (-d, +d), **kwargs)
ax.plot((1-d, 1+d), (1-d, 1+d), **kwargs)

kwargs.update(transform=ax2.transAxes) 
ax2.plot((-d, +d), (1-d, 1+d), **kwargs)
ax2.plot((-d, +d), (-d, +d), **kwargs)

plt.legend(fontsize=fontsize-2)
plt.savefig("dosphonons-BEEFtop.pdf")
plt.show()
