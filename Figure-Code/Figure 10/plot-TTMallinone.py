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

file_40 = "/dipc/inakiferte/vdW-DF/Pt_CO_eph/Wannier/preinterpol/TTM_results/LinPRB2008/F40Jm-2/F40.dat"
file_80 = "/dipc/inakiferte/vdW-DF/Pt_CO_eph/Wannier/preinterpol/TTM_results/LinPRB2008/F80Jm-2/F80.dat"
file_130 = "/dipc/inakiferte/vdW-DF/Pt_CO_eph/Wannier/preinterpol/TTM_results/LinPRB2008/F130Jm-2/F130.dat"


time_40 = np.loadtxt(file_40)[:,0] #Time for F40
Te_40   = np.loadtxt(file_40)[:,1] #Te for F40
Tl_40   = np.loadtxt(file_40)[:,2] #Tl for F40

time_80 = np.loadtxt(file_80)[:,0] #Time for F80
Te_80   = np.loadtxt(file_80)[:,1] #Te for F80
Tl_80   = np.loadtxt(file_80)[:,2] #Tl for F80

time_130 = np.loadtxt(file_130)[:,0] #Time for F130
Te_130   = np.loadtxt(file_130)[:,1] #Te for F130
Tl_130   = np.loadtxt(file_130)[:,2] #Tl for F130


#Plot

fontsize=15


plt.figure(figsize = (12,6))


plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True, top=True, direction='out')

plt.ylabel("$T(10^{3}K)$",fontsize=fontsize)
plt.xlabel("t (ps)",fontsize=fontsize)
plt.plot(time_40*10**(-3), Te_40*10**(-3),color="blue", label='$F=40~J/m^{2}$')
plt.plot(time_40*10**(-3), Tl_40*10**(-3),color="blue",linestyle='dashed', label='$F=40~J/m^{2}$')
plt.plot(time_80*10**(-3), Te_80*10**(-3),color="orange", label='$F=80~J/m^{2}$')
plt.plot(time_80*10**(-3), Tl_80*10**(-3),color="orange",linestyle='dashed', label='$F=80~J/m^{2}$')
plt.plot(time_130*10**(-3), Te_130*10**(-3),color="green", label='$F=130~J/m^{2}$')
plt.plot(time_130*10**(-3), Tl_130*10**(-3),color="green",linestyle='dashed',label='$F=130~J/m^{2}$')

plt.legend(fontsize=fontsize-2)


plt.savefig('TTM-plot.pdf', bbox_inches='tight')
plt.show()



