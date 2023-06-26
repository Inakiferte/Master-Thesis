import numpy as np
import matplotlib.pyplot as plt 
import os, sys
import subprocess
import pathlib

# Define the working directory
DIR = pathlib.Path().absolute()

print("Reading data...")
#Lets import the fits data


data_filePBE_MLWFs= "/scratch/inakiferte/CO_on_Pt/PBE/Pt_CO_eph/Wannier/Wannier-Bands/epw/nbnd-81/Ptbulk_band.dat"
data_filePBE_BANDS= "/scratch/inakiferte/CO_on_Pt/PBE/Pt_CO_eph/Wannier/Wannier-Bands/epw/nbnd-81/bands.dat.gnu"
data_filePBE_Err = "/scratch/inakiferte/CO_on_Pt/PBE/Pt_CO_eph/Wannier/Wannier-Bands/epw/nbnd-81/bands-join.dat"


#data_filevdW_MLWFs = "/scratch/inakiferte/CO_on_Pt/vdW-DF/Pt_CO_eph/CO_TOP/Wannier/epw/nbnd-81/Ptbulk_band.dat"
#data_filevdW_BANDS = "/scratch/inakiferte/CO_on_Pt/vdW-DF/Pt_CO_eph/CO_TOP/Wannier/epw/nbnd-81/bands.dat.gnu" 
#data_filevdW_Err = "/scratch/inakiferte/CO_on_Pt/vdW-DF/Pt_CO_eph/CO_TOP/Wannier/epw/nbnd-81/bands-join.dat"

#data_fileBEEF_MLWFs = "/scratch/inakiferte/CO_on_Pt/BEEF-vdW/Pt_CO_eph/CO_Top/Wannier/Wannier-Bands/epw/nbnd-81/Ptbulk_band.dat"
#data_fileBEEF_BANDS = "/scratch/inakiferte/CO_on_Pt/BEEF-vdW/Pt_CO_eph/CO_Top/Wannier/Wannier-Bands/epw/nbnd-81/bands.dat.gnu"
#data_fileBEEF_Err = "/scratch/inakiferte/CO_on_Pt/BEEF-vdW/Pt_CO_eph/CO_Top/Wannier/Wannier-Bands/epw/nbnd-81/bands-join.dat"

with open(data_filePBE_MLWFs) as f:
    PBE_MLWFs = np.loadtxt(f,skiprows=0) 
with open(data_filePBE_BANDS) as f:
    PBE_BANDS = np.loadtxt(f,skiprows=0)
with open(data_filePBE_Err) as f:
    PBE_Err = np.loadtxt(f,skiprows=0)

#with open(data_filevdW_MLWFs) as f:
#    vdW_MLWFs = np.loadtxt(f,skiprows=0)
#with open(data_filevdW_BANDS) as f:
#    vdW_BANDS = np.loadtxt(f,skiprows=0)
#with open(data_filevdW_Err) as f:
#    vdW_Err = np.loadtxt(f,skiprows=0)

#with open(data_fileBEEF_MLWFs) as f:
#    BEEF_MLWFs = np.loadtxt(f,skiprows=0)
#with open(data_fileBEEF_BANDS) as f:
#    BEEF_BANDS = np.loadtxt(f,skiprows=0)
#with open(data_fileBEEF_Err) as f:
#    BEEF_Err = np.loadtxt(f,skiprows=0)

print("Data readed!")

PBE_Fermi = 5.26615
vdW_Fermi = 4.6781
BEEF_Fermi = 4.7505
k_tot = 77
n_block = 81
#Plot
fontsize=15

plt.figure(figsize = (12,6))
grid = plt.GridSpec(1,2, wspace = 0.3)

ax01=plt.subplot(grid[0,0])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True, top=True, direction='out')
plt.ylabel("$E-E_{F}~(eV)$",fontsize=fontsize)
#plt.axhline(PBE_Fermi,0.0,color="red", linewidth=2.0)
#plt.text(0.2, PBE_Fermi + 0.2, 'Fermi Level', ha='center', va='bottom',
#fontsize=10, color="red")
plt.text(0.0, -4.5, 'G', ha='center', va='bottom', fontsize=fontsize)
plt.axvline(x=0.5/PBE_BANDS[-1,0]*PBE_MLWFs[-1,0],color="black",linewidth=0.5)
plt.text(0.5/PBE_BANDS[-1,0]*PBE_MLWFs[-1,0], -4.5, 'M', ha='center', va='bottom',fontsize=fontsize)
plt.axvline(x=0.966/PBE_BANDS[-1,0]*PBE_MLWFs[-1,0],color="black",linewidth=0.5)
plt.text(0.966/PBE_BANDS[-1,0]*PBE_MLWFs[-1,0], -4.5, 'K', ha='center', va='bottom',fontsize=fontsize)
plt.text(PBE_MLWFs[-1,0], -4.5, 'G', ha='center',va='bottom',fontsize=fontsize)
plt.xlim(0.0,PBE_MLWFs[-1,0])
plt.ylim(-4.0,4.0)

plt.scatter(PBE_BANDS[:,0]/PBE_BANDS[-1,0]*PBE_MLWFs[-1,0],
PBE_BANDS[:,1]-PBE_Fermi, color = "darkorange",s=15, label
= "DFT")
inicio = 0
fin = k_tot
x = PBE_MLWFs[inicio:fin, 0]
y = PBE_MLWFs[inicio:fin, 1]
plt.plot(x, y-PBE_Fermi, color="blue", label="MLWFs")
for i in range(1,n_block+1):
    inicio = i * k_tot
    fin = inicio + k_tot
    x = PBE_MLWFs[inicio:fin, 0]
    y = PBE_MLWFs[inicio:fin, 1]
    plt.plot(x, y-PBE_Fermi, color="blue")

plt.xticks([])
plt.legend(fontsize=fontsize-2)

ax02=plt.subplot(grid[0,1])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True, top=True, direction='out')
plt.ylabel("$E_{MLWFs}-E_{DFT}$ (eV)",fontsize=fontsize)
plt.xlabel("$E-E_{F}$ (eV)", fontsize=fontsize)
plt.xlim(-10,PBE_Err[-1,1]-PBE_Fermi)
plt.ylim(0.0,0.06)
plt.scatter(PBE_Err[:,1]-PBE_Fermi, np.abs(PBE_Err[:,1]-PBE_Err[:,3]),
color="green", s=5)

#ax01=plt.subplot(grid[0,0])
#plt.tick_params(axis='both', which='both',length=3, width=1.0,
#labelsize=15, right=True, top=True, direction='out')
#plt.ylabel("$E-E_{F}~(eV)$",fontsize=fontsize)
#plt.axhline(vdW_Fermi,0.0,color="red", linewidth=2.0)
#plt.text(0.2, vdW_Fermi + 0.2, 'Fermi Level', ha='center', va='bottom',
#fontsize=10, color="red")
#plt.text(0.0, -4.5, 'G', ha='center', va='bottom', fontsize=fontsize)
#plt.axvline(x=0.5/vdW_BANDS[-1,0]*vdW_MLWFs[-1,0],color="black",linewidth=0.5)
#plt.text(0.5/vdW_BANDS[-1,0]*vdW_MLWFs[-1,0], -4.5, 'M', ha='center',
#va='bottom',fontsize=fontsize)
#plt.axvline(x=0.966/vdW_BANDS[-1,0]*vdW_MLWFs[-1,0],color="black",linewidth=0.5)
#plt.text(0.966/vdW_BANDS[-1,0]*vdW_MLWFs[-1,0],-4.5, 'K', ha='center',
#va='bottom',fontsize=fontsize)
#plt.text(vdW_MLWFs[-1,0], -4.5, 'G',
#ha='center',va='bottom',fontsize=fontsize)
#plt.xlim(0.0,vdW_MLWFs[-1,0])
#plt.ylim(-4.0,4.0)

#plt.scatter(vdW_BANDS[:,0]/vdW_BANDS[-1,0]*vdW_MLWFs[-1,0],
#vdW_BANDS[:,1]-vdW_Fermi, color = "darkorange",s=15, label
#= "DFT")
#inicio = 0
#fin = k_tot
#x = vdW_MLWFs[inicio:fin, 0]
#y = vdW_MLWFs[inicio:fin, 1]
#plt.plot(x, y-vdW_Fermi, color="blue", label="MLWFs")
#for i in range(1,n_block+1):
#    inicio = i * k_tot
#    fin = inicio + k_tot
#    x = vdW_MLWFs[inicio:fin, 0]
#    y = vdW_MLWFs[inicio:fin, 1]
#    plt.plot(x, y-vdW_Fermi, color="blue")

#plt.xticks([])
#plt.legend(fontsize=fontsize-2)

#ax02=plt.subplot(grid[0,1])
#plt.tick_params(axis='both', which='both',length=3, width=1.0,
#labelsize=15, right=True, top=True, direction='out')
#plt.ylabel("$E_{MLWFs}-E_{DFT}$ (eV)",fontsize=fontsize)
#plt.xlabel("$E-E_{F}$ (eV)", fontsize=fontsize)
#plt.ylim(0.0,0.06)
#plt.xlim(-9,5)
#plt.scatter(vdW_Err[:,1]-vdW_Fermi, np.abs(vdW_Err[:,1]-vdW_Err[:,3]),
#color="green", s=5)

#ax01=plt.subplot(grid[0,0])
#plt.tick_params(axis='both', which='both',length=3, width=1.0,
#labelsize=15, right=True, top=True, direction='out')
#plt.ylabel("$E-E_{F}~(eV)$",fontsize=fontsize)
#plt.axhline(BEEF_Fermi,0.0,color="red", linewidth=2.0)
#plt.text(0.2, BEEF_Fermi + 0.2, 'Fermi Level', ha='center', va='bottom',
#fontsize=10, color = "red")
#plt.text(0.0, -4.5, 'G', ha='center', va='bottom', fontsize=fontsize)
#plt.axvline(x=0.5/BEEF_BANDS[-1,0]*BEEF_MLWFs[-1,0],color="black",linewidth=0.5)
#plt.text(0.5/BEEF_BANDS[-1,0]*BEEF_MLWFs[-1,0], -4.5, 'M', ha='center',
#va='bottom',fontsize=fontsize)
#plt.axvline(x=0.966/BEEF_BANDS[-1,0]*BEEF_MLWFs[-1,0],color="black",linewidth=0.5)
#plt.text(0.966/BEEF_BANDS[-1,0]*BEEF_MLWFs[-1,0], -4.5, 'K', ha='center',
#va='bottom',fontsize=fontsize)
#plt.text(BEEF_MLWFs[-1,0], -4.5, 'G',
#ha='center',va='bottom',fontsize=fontsize)
#plt.xlim(0.0,BEEF_MLWFs[-1,0])
#plt.ylim(-4.0,4.0)
#plt.scatter(BEEF_BANDS[:,0]/BEEF_BANDS[-1,0]*BEEF_MLWFs[-1,0],
#BEEF_BANDS[:,1]-BEEF_Fermi, color = "darkorange",s=15, label
#= "DFT")
#inicio = 0
#fin = k_tot
#x = BEEF_MLWFs[inicio:fin, 0]
#y = BEEF_MLWFs[inicio:fin, 1]
#plt.plot(x, y-BEEF_Fermi, color="blue", label="MLWFs")
#for i in range(1,n_block+1):
#    inicio = i * k_tot
#    fin = inicio + k_tot
#    x = BEEF_MLWFs[inicio:fin, 0]
#    y = BEEF_MLWFs[inicio:fin, 1]
#    plt.plot(x, y-BEEF_Fermi, color="blue")



#plt.xticks([])
#plt.legend(fontsize=fontsize-2)

#ax02=plt.subplot(grid[0,1])
#plt.tick_params(axis='both', which='both',length=3, width=1.0,
#labelsize=15, right=True, top=True, direction='out')
#plt.ylabel("$E_{MLWFs}-E_{DFT}$ (eV)",fontsize=fontsize)
#plt.xlabel("$E-E_{F}$ (eV)", fontsize=fontsize)
#plt.xlim(-9,5)
#plt.ylim(0.0,0.06)
#plt.scatter(BEEF_Err[:,1]-BEEF_Fermi, np.abs(BEEF_Err[:,1]-BEEF_Err[:,3]),
#color="green", s=5)
##
##
##
plt.savefig("MLWFs-PBEv2.pdf", bbox_inches='tight')
plt.show()
