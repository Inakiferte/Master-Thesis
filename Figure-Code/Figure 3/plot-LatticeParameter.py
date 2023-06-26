import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import PercentFormatter
import numpy as np

# To use bash commands
import os, sys
import subprocess

# To obtain path of notebook
import pathlib
from scipy import optimize
from scipy import special


#Read data

file_BEEF = "/dipc/inakiferte/BEEF-vdW/BULK/a-lattice_Convergence_adjustment/Results/a-BEEFvdW.dat"
file_PBE  = "/dipc/inakiferte/PBE/BULK/a-lattice_Convergence_adjustment/Results/a-PBE.dat"
file_vdW  = "/dipc/inakiferte/vdW-DF/Bulk/a-lattice_Convergence/a-vdW-DF.dat"


a_BEEF   = np.loadtxt(file_BEEF)[:,0] #Lattice parameter for BEEF
E_BEEF   = np.loadtxt(file_BEEF)[:,1] #Energy of the scf for BEEF

a_PBE    = np.loadtxt(file_PBE)[:,0]  #Lattice parameter for PBE
E_PBE    = np.loadtxt(file_PBE)[:,1]  #Energy of the scf for PBE

a_vdW    = np.loadtxt(file_vdW)[:,0]  #Lattice parameter for vdW
E_vdW    = np.loadtxt(file_vdW)[:,1]  #Energy of the scf for vdW


#Plot

fontsize=15


plt.figure(figsize = (12,6))
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True, top=True, direction='out')
plt.ylabel("$E_{bulk}-E_{min}~(10^{-4}~Ry)$",fontsize=fontsize)
plt.xlabel("$a~(a_{B})$",fontsize=fontsize)

plt.plot(a_PBE, (E_PBE-E_PBE[0])*10**(4), label="PBE", color="darkorange" )
plt.scatter(a_PBE, (E_PBE-E_PBE[0])*10**(4), marker="o",color="darkorange")

plt.plot(a_vdW, (E_vdW-E_vdW[0])*10**(4), label="vdW-DF",
color= "green")
plt.scatter(a_vdW, (E_vdW-E_vdW[0])*10**(4), marker="o", color="green")

plt.plot(a_BEEF, (E_BEEF-E_BEEF[0])*10**(4), label="BEEF-vdW",
color="blue")
plt.scatter(a_BEEF, (E_BEEF-E_BEEF[0])*10**(4), marker="o", color="blue")


#grid = plt.GridSpec(1, 3, wspace = 0.35)


#ax01=plt.subplot(grid[0])
#plt.ylabel("$E-E_{min}~(10^{-4}~Ryd)$",fontsize=fontsize)
#plt.xlabel("$a~(a_{B})$",fontsize=fontsize)
#plt.plot(a_BEEF, (E_BEEF-E_BEEF[0])*10**(4))
#plt.scatter(a_BEEF, (E_BEEF-E_BEEF[0])*10**(4))
#plt.title("BEEF-vdW Lattice Parameter")



#ax02=plt.subplot(grid[1])
#plt.ylabel("$E-E_{min}~(10^{-4}~Ryd)$",fontsize=fontsize)
#plt.xlabel("$a~(a_{B})$",fontsize=fontsize)
#plt.plot(a_PBE, (E_PBE-E_PBE[0])*10**(4))
#plt.title("PBE Lattice Parameter")


#ax03=plt.subplot(grid[2])
#plt.ylabel("$E-E_{min}~(10^{-4}~Ryd)$",fontsize=fontsize)
#plt.xlabel("$a~(a_{B})$",fontsize=fontsize)
#plt.plot(a_vdW, (E_vdW-E_vdW[0])*10**(4))
#plt.title("vdW-DF Lattice Parameter")

plt.legend(fontsize=fontsize-2)
plt.savefig('Lattice-Parameter-Functionals.pdf')
plt.show()



