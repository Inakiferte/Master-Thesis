import numpy as np
import matplotlib.pyplot as plt 
import os, sys
import subprocess
import pathlib

# Define the working directory
DIR = pathlib.Path().absolute()

print("adjust cutoff")
#Lets import the fits data


data_file1 = "/dipc/inakiferte/PBE/Pt_CO_relax/ecutrho-convergence/ecutoff-ecutrho.dat"
data_file2 = "/dipc/inakiferte/PBE/Pt_CO_relax/ecutwcf-convergence/ecutoff-ecutwcf.dat"
data_file3 = "/dipc/inakiferte/PBE/Pt_CO_relax/k-points/k-points.dat"
with open(data_file1) as f:
    Ecutoff1 = np.loadtxt(f,skiprows=0) 

with open(data_file2) as f:
    Ecutoff2 = np.loadtxt(f,skiprows=0)
with open(data_file3) as f:
    Kpoints = np.loadtxt(f,skiprows=0)



#Plot
fontsize=15

plt.figure(figsize = (12,6))
grid = plt.GridSpec(1,3, wspace = 0.4)

ax01=plt.subplot(grid[2])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True, top=True, direction='out')
plt.xlabel("$1/E_{cutrho}~(Ry^{-1}$)",fontsize=fontsize)
plt.ylabel("$E_{surface} - E_{lim}~(Ry)$",fontsize=fontsize)
plt.text(0.002, 0.035, '(c)', ha='center', va='bottom', fontsize=fontsize)
plt.plot(1./Ecutoff1[:-1,0], abs(Ecutoff1[:-1,2]-Ecutoff1[-1,2]),linewidth=1,marker='o',markersize=3)
plt.plot(1./Ecutoff1[:-1,0], 1e-3*np.ones_like(Ecutoff1[:-1,2]))
plt.yscale("log")


ax02=plt.subplot(grid[1])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True, top=True, direction='out')
plt.text(0.01, 3.5, '(b)', ha='center', va='bottom', fontsize=fontsize)
plt.xlabel("$1/E_{cut}~(Ry^{-1}$)",fontsize=fontsize)
plt.ylabel("$E_{surface} - E_{lim}~(Ry)$",fontsize=fontsize)
plt.plot(1./Ecutoff2[:-1,0], abs(Ecutoff2[:-1,2]-Ecutoff2[-1,2]),linewidth=1,marker='o',markersize=3)
plt.plot(1./Ecutoff2[:-1,0], 1e-3*np.ones_like(Ecutoff2[:-1,2]))
plt.yscale("log")

ax03=plt.subplot(grid[0])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True, top=True, direction='out')
plt.text(0.1, 0.05, '(a)', ha='center', va='bottom', fontsize=fontsize)
plt.xlabel("1/K ($a_{B}^{-1}$)",fontsize=fontsize)
plt.ylabel("$E_{surface} - E_{lim}~(Ry)$",fontsize=fontsize)
plt.plot(1./Kpoints[:-1,0], abs(Kpoints[:-1,2]-Kpoints[-1,2]),linewidth=1,marker='o',markersize=3)
plt.plot(1./Kpoints[:-1,0], 1e-3*np.ones_like(Kpoints[:-1,2]))
plt.yscale("log")

print("Kpoints limit value and energy are")
print(Kpoints[-1,0], Kpoints[-1,2])
print("Ecutwfc limit value and energy are")
print(Ecutoff2[-1,0], Ecutoff2[-1,2])
print("Ecutrho limit value and energy are")
print(Ecutoff1[-1,0], Ecutoff1[-1,2])


plt.savefig("convergence-ecutrho.pdf", bbox_inches='tight')
plt.show()
