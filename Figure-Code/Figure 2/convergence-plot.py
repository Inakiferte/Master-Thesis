import numpy as np
import matplotlib.pyplot as plt 
import os, sys
import subprocess
import pathlib

# Define the working directory
DIR = pathlib.Path().absolute()

print("adjust cutoff")
#Lets import the fits data
#The structure is {rho_min_x} {rho_max_x} {a_s[i]} {popt[0]} {popt[1]} {popt[2]} {n_c}

data_file='k.dat'
full_path = os.path.join(DIR,data_file)
with open(full_path) as f:
    Ekpoints = np.loadtxt(f,skiprows=0)  

data_file='cutoff.dat'
full_path = os.path.join(DIR,data_file)
with open(full_path) as f:
    Ecutoff = np.loadtxt(f,skiprows=0) 

fontsize=15

plt.figure(figsize = (12,6))
grid = plt.GridSpec(1, 2, wspace = 0.3, width_ratios=[1,1])

ax01=plt.subplot(grid[1])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True, top=True, direction='out')
plt.xlabel("$1/E_{cut}~(Ry^{-1}$)",fontsize=fontsize)
plt.ylabel("$E_{bulk} - E_{lim}~(Ry)$",fontsize=fontsize)
plt.text(0.01, 0.5, '(b)', ha='center', va='bottom', fontsize=fontsize)
plt.plot(1./Ecutoff[:-1,0], abs(Ecutoff[:-1,2]-Ecutoff[-1,2]),linewidth=1,marker='o',markersize=3)
plt.plot(1./Ecutoff[:-1,0], 1e-4*np.ones_like(Ecutoff[:-1,2]))
plt.yscale("log")

ax02=plt.subplot(grid[0])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True, top=True, direction='out')
plt.text(0.1, 0.3, '(a)', ha='center', va='bottom', fontsize=fontsize)
plt.xlabel("$1/K~(a_{B}^{-1}$)",fontsize=fontsize)
plt.ylabel("$E_{bulk} - E_{lim}~(Ry)$",fontsize=fontsize)


plt.plot(1./Ekpoints[:-1,0], abs(Ekpoints[:-1,2]-Ekpoints[-1,2]),linewidth=1,marker='o',markersize=3)
plt.plot(1./Ekpoints[:-1,0], 1e-4*np.ones_like(Ekpoints[:-1,2]))
plt.yscale("log")

print("K-point limit energy and value")
print(Ekpoints[-1,2],Ekpoints[-1,0])
print("Cutoff limit energy and value")
print(Ecutoff[-1,2],Ecutoff[-1,0])

plt.savefig("Conver-Cutoff-Kpoints.pdf", bbox_inches='tight')
plt.show()
