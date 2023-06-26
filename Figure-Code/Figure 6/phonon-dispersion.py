import numpy as np
import matplotlib.pyplot as plt 
import os, sys
import subprocess
import pathlib

# Define the working directory
DIR = pathlib.Path().absolute()

print("Reading data...")
#Lets import the fits data

modes = 42
data_file1 = "/dipc/inakiferte/PBE/Pt_CO_eph/phonons/results_ph_scf1_qgrid6_final/Ptbulk.freq.gp"
data_file2 = "/dipc/inakiferte/PBE/Pt_CO_eph/phonons/results_ph_scf2_qgrid6_final/Ptbulk.freq.gp"
with open(data_file1) as f:
    phonon6 = np.loadtxt(f,skiprows=0) 

with open(data_file2) as f:
    phonon8 = np.loadtxt(f,skiprows=0)


cm_inverse_to_eV = 1.23984*10**(-4)
print("Data readed!")
#Plot
fontsize=15

plt.figure(figsize = (12,6))

plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True, top=False, direction='in')
plt.ylabel("$\hbar\omega$ (meV)",fontsize=fontsize)
plt.text(0.0, -8, 'G', ha='center', va='bottom', fontsize=fontsize)

plt.axvline(x=0.5,color="black",linewidth=0.5)
plt.text(0.5, -8, 'M', ha='center', va='bottom',fontsize=fontsize)

plt.axvline(x=0.966,color="black",linewidth=0.5)
plt.text(0.966, -8, 'K', ha='center', va='bottom',fontsize=fontsize)

plt.text(phonon6[-1,0], -8, 'G', ha='center', va='bottom',fontsize=fontsize)
plt.xlim(0.0,phonon6[-1,0])
plt.plot(phonon6[:,0],phonon6[:,1] * cm_inverse_to_eV * 10 ** (3), color="blue",label="$K_{SCF}=6X6X1$")
plt.scatter(phonon8[:,0],phonon8[:,1] * cm_inverse_to_eV * 10 ** (3),
color="darkorange",s=15,label="$K_{SCF}=8X8X1$")
plt.xticks([])


for i in range(2,modes):
 plt.plot(phonon6[:,0],phonon6[:,i] * cm_inverse_to_eV * 10 ** (3), color="blue")
 plt.scatter(phonon8[:,0],phonon8[:,i] * cm_inverse_to_eV * 10 ** (3), color="darkorange", s=15)
 print((phonon6[:,i]- phonon8[:,i]) * cm_inverse_to_eV * 10 ** (3))
 plt.legend(fontsize=fontsize-2)
plt.savefig("phonon_dispersion_comparation.pdf", bbox_inches='tight')
plt.show()
