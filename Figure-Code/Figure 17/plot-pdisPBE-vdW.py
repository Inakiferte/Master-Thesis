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

data_PBE = "/scratch/inakiferte/CO_on_Pt/PBE/phonons/results_ph_scf1_qgrid6_final/Ptbulk.freq.gp"

data_vdW = "/scratch/inakiferte/CO_on_Pt/vdW-DF/results_ph_scf1_qgrid6_final/Ptbulk.freq.gp"

with open(data_PBE) as f:
    PBE = np.loadtxt(f,skiprows=0) 

with open(data_vdW) as f:
    vdW = np.loadtxt(f,skiprows=0)

freqPBE = PBE[:,0]
freqvdW = vdW[:,0]
print("Data readed!")

#Plot
fontsize=15

plt.figure(figsize = (12,6))
grid = plt.GridSpec(1, 2, wspace = 0.3)

ax01=plt.subplot(grid[0])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=False, top=True, direction='out')
plt.ylabel("$\omega~(cm^{-1})$", fontsize=fontsize)
plt.xlim(0,PBE[-1,0])
plt.ylim(-100,500)
#G point
plt.text(0.0, -150, 'G', ha='center', va='bottom', fontsize=fontsize)
#M point
plt.axvline(x=0.5,color="black",linewidth=0.5)
plt.text(0.5, -150, 'M', ha='center', va='bottom',fontsize=fontsize)
#K point
plt.axvline(x=0.966,color="black",linewidth=0.5)
plt.text(0.966, -150, 'K', ha='center', va='bottom',fontsize=fontsize)
plt.text(1.20, 420, '(a)', ha='center', va='bottom',fontsize=fontsize)

#G point
plt.text(PBE[-1,0], -150, 'G', ha='center', va='bottom',fontsize=fontsize)
for i in range(1,modes+1):
 plt.plot(freqPBE,PBE[:,i], color="blue")
plt.xticks([])
# zoom-in / limit the view to different portions of the data
ax02=plt.subplot(grid[1])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=False, top=True, direction='out')
plt.xlim(0,vdW[-1,0])
plt.ylim(-100,500)
plt.ylabel("$\omega~(cm^{-1})$", fontsize=fontsize)
plt.text(0.0, -150, 'G', ha='center', va='bottom', fontsize=fontsize)

#G point
plt.text(0.0, -150, 'G', ha='center', va='bottom', fontsize=fontsize)
#M point
plt.axvline(x=0.5,color="black",linewidth=0.5)
plt.text(0.5, -150, 'M', ha='center', va='bottom',fontsize=fontsize)
#K point
plt.axvline(x=0.966,color="black",linewidth=0.5)
plt.text(0.966, -150, 'K', ha='center', va='bottom',fontsize=fontsize)

#G point
plt.text(vdW[-1,0], -150, 'G', ha='center',
va='bottom',fontsize=fontsize)
for i in range(1,modes+1):
  plt.plot(freqvdW,vdW[:,i], color="darkorange")

plt.text(1.20, 420, '(b)', ha='center', va='bottom',fontsize=fontsize)
plt.xticks([])



#plt.legend()
plt.savefig("dispersion-phononPBE-vdW.pdf")
plt.show()
