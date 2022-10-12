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
grid = plt.GridSpec(1, 2, hspace = 0.0, width_ratios=[1,1])

ax01=plt.subplot(grid[0])
plt.xlabel("1/E_cut (Ryd$^{-1}$)",fontsize=fontsize)
plt.ylabel("$E - E_{lim}$",fontsize=fontsize)
plt.plot(1./Ecutoff[:-1,0], abs(Ecutoff[:-1,2]-Ecutoff[-1,2]),linewidth=1,marker='o',markersize=3)
plt.plot(1./Ecutoff[:-1,0], 1e-4*np.ones_like(Ecutoff[:-1,2]),linewidth=1,marker='o',markersize=3)
plt.yscale("log")


ax02=plt.subplot(grid[1])
plt.xlabel("1/k (Ryd$^{-1}$)",fontsize=fontsize)
plt.ylabel("$E - E_{lim}$",fontsize=fontsize)


plt.plot(1./Ekpoints[:-1,0], abs(Ekpoints[:-1,2]-Ekpoints[-1,2]),linewidth=1,marker='o',markersize=3)
plt.plot(1./Ekpoints[:-1,0], 1e-4*np.ones_like(Ekpoints[:-1,2]),linewidth=1,marker='o',markersize=3)
plt.yscale("log")


plt.savefig("convergence.pdf", bbox_inches='tight')
plt.show()
