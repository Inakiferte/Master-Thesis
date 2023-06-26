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

print("Here we plot the DOS for the CO on atop position for PBE functional")

#Read data

file_dostot = "/dipc/inakiferte/PBE/Pt_CO_relax/CO_Top/Pt_CO_DOS/nscf_PBE_PtCO_Top_12/dos_tot.dat"
file_dosd = "/dipc/inakiferte/PBE/Pt_CO_relax/CO_Top/Pt_CO_DOS/nscf_PBE_PtCO_Top_12/dos_d.dat"
file_doss = "/dipc/inakiferte/PBE/Pt_CO_relax/CO_Top/Pt_CO_DOS/nscf_PBE_PtCO_Top_12/dos_s.dat"
file_dosOs = "/dipc/inakiferte/PBE/Pt_CO_relax/CO_Top/Pt_CO_DOS/nscf_PBE_PtCO_Top_12/dos_Os.dat"
file_dosOp = "/dipc/inakiferte/PBE/Pt_CO_relax/CO_Top/Pt_CO_DOS/nscf_PBE_PtCO_Top_12/dos_Op.dat"
file_dosCs = "/dipc/inakiferte/PBE/Pt_CO_relax/CO_Top/Pt_CO_DOS/nscf_PBE_PtCO_Top_12/dos_Cs.dat"
file_dosCp = "/dipc/inakiferte/PBE/Pt_CO_relax/CO_Top/Pt_CO_DOS/nscf_PBE_PtCO_Top_12/dos_Cp.dat"



#Surface only
file_surface = "/scratch/inakiferte/CO_on_Pt/PBE/Pt_Scf/scf_1/nscf_1/dos_tot.dat"
file_surfaces = "/scratch/inakiferte/CO_on_Pt/PBE/Pt_Scf/scf_1/nscf_1/dos_s.dat"
file_surfaced = "/scratch/inakiferte/CO_on_Pt/PBE/Pt_Scf/scf_1/nscf_1/dos_d.dat"
##############

Energy = np.loadtxt(file_dostot)[:,0] #Energy
Energyd = np.loadtxt(file_dosd)[:,0]
dostot = np.loadtxt(file_dostot)[:,1] #Total DOS
dosdz2 = np.loadtxt(file_dosd)[:,2] #dz2 PDOS
dosdzx = np.loadtxt(file_dosd)[:,3] #dzx PDOS
dosdzy = np.loadtxt(file_dosd)[:,4] #dzy PDOS
dosx2y2 = np.loadtxt(file_dosd)[:,5] # dx2-y2
dosxy = np.loadtxt(file_dosd)[:,6] # dxy
doss = np.loadtxt(file_doss)[:,1] #s
Energys = np.loadtxt(file_doss)[:,0]  #Energy

EnergyOs = np.loadtxt(file_dosOs)[:,0]  #Energy
dostotOs = np.loadtxt(file_dosOs)[:,1]  #Energy

EnergyCs = np.loadtxt(file_dosCs)[:,0]  #Energy
dostotCs = np.loadtxt(file_dosCs)[:,1]  #Energy

EnergyOp = np.loadtxt(file_dosOp)[:,0]
dosOpz = np.loadtxt(file_dosOp)[:,2]  #Energy
dosOpx = np.loadtxt(file_dosOp)[:,3]  #Energy
dosOpy = np.loadtxt(file_dosOp)[:,4]  #Energy

EnergyCp = np.loadtxt(file_dosCp)[:,0]
dosCpz = np.loadtxt(file_dosCp)[:,2]  #Energy
dosCpx = np.loadtxt(file_dosCp)[:,3]  #Energy
dosCpy = np.loadtxt(file_dosCp)[:,4]  #Energy

Efermi = 5.264 # in eV

#Surface only 
EnergySur = np.loadtxt(file_surface)[:,0] #Energy
dosSur = np.loadtxt(file_surface)[:,1] #DOS

EnergySurd = np.loadtxt(file_surfaced)[:,0] #Energy
dosSurtotd = np.loadtxt(file_surfaced)[:,1] #Energy
dosSurdz2 = np.loadtxt(file_surfaced)[:,2] #dz2 PDOS
dosSurdzx = np.loadtxt(file_surfaced)[:,3] #dzx PDOS
dosSurdzy = np.loadtxt(file_surfaced)[:,4] #dzy PDOS
dosSurx2y2 = np.loadtxt(file_surfaced)[:,5] # dx2-y2
dosSurxy = np.loadtxt(file_surfaced)[:,6] # dxy



EnergySurs = np.loadtxt(file_surfaces)[:,0] #Energy
dosSurs = np.loadtxt(file_surfaces)[:,1] #Energy

EfermiSur =  4.619 # in eV

#Plot

fontsize=15
plt.figure(figsize = (12,6))
grid = plt.GridSpec(6, 1, hspace = 0.0)



ax01=plt.subplot(grid[5,0])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True, top=False, direction='in')

plt.xlabel("$E-E_{F}$ (eV)", fontsize=fontsize)
plt.plot(EnergySur - EfermiSur, dosSur, linestyle="dashed", color="blue")
plt.plot(Energy - Efermi, dostot, label="total" , color="blue")
plt.fill_between(Energy - Efermi, 0, dostot, where=(Energy < Efermi),
alpha=0.25, facecolor='blue')
plt.legend(fontsize=fontsize-2, loc='upper right')
plt.xlim(-12.5,5)
plt.ylim(0,)



ax02=plt.subplot(grid[2,0])
plt.tick_params(axis='both', which='both',length=5, width=1.0,
labelsize=15, right=True, top=True, direction='in')
plt.xticks([])
#plt.ylabel("DOS (states/eV)",fontsize=fontsize)

plt.plot(EnergySurd - EfermiSur, dosSurx2y2,
color="orange", linestyle="dashed" )
plt.plot(Energyd - Efermi, dosx2y2, label="$d_{x^{2}-y^{2}}$", color="orange" )
plt.fill_between(Energyd - Efermi, 0, dosx2y2, where=(Energyd < Efermi),
alpha=0.25, facecolor='orange')
plt.legend(fontsize=fontsize-2, loc='upper right')
plt.xlim(-12.5,5)
plt.ylim(0,)

ax03=plt.subplot(grid[1,0])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True, top=True, direction='in')
plt.xticks([])
#plt.ylabel("DOS(E)",fontsize=fontsize)
plt.plot(EnergySurd - EfermiSur, dosSurdzx + dosSurdzy,
color="red", linestyle="dashed" )
plt.plot(Energyd - Efermi, dosdzx + dosdzy, label="$d_{zx} + d_{zy}$",
color="red" )
plt.fill_between(Energyd - Efermi, 0, dosdzx + dosdzy, where=(Energyd < Efermi),
alpha=0.25, facecolor='red')
plt.legend(fontsize=fontsize-2, loc='upper right')
plt.xlim(-12.5,5)
plt.ylim(0,)

ax04=plt.subplot(grid[3,0])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True, top=True, direction='in')
plt.xticks([])
plt.ylabel("DOS (states/eV)",fontsize=fontsize)

plt.plot(EnergySurs - EfermiSur, dosSurs,
color="purple",linestyle="dashed")
plt.plot(Energys - Efermi, doss, label="s",
color="purple" )
plt.fill_between(Energys - Efermi, 0, doss, where=(Energys <
Efermi),
alpha=0.25, facecolor='purple')
plt.legend(loc='upper right',fontsize=fontsize-2)
plt.xlim(-12.5,5)
plt.ylim(0,)

ax05=plt.subplot(grid[4,0])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True, top=True, direction='in')
plt.xticks([])

plt.plot(EnergyCp - Efermi, dosCpz + dostotCs + dosOpz + dostotOs ,
label="$\sigma$ character",
color="black")
plt.fill_between(EnergyCp - Efermi, 0, dosCpz + dostotCs + dosOpz +
dostotOs, where=(EnergyCp <
Efermi),
alpha=0.25, facecolor='black')

#plt.plot(EnergyCp - Efermi, dosCpx, label="C-px",
#color="purple", linestyle="dashed" )
#plt.fill_between(EnergyCp - Efermi, 0, dosCpx, where=(EnergyCp <
#Efermi),
#alpha=0.25, facecolor='purple')

#plt.plot(EnergyCp - Efermi, dosCpy, label="C-py",
#color="green" , linestyle="dashed")
#plt.fill_between(EnergyCp - Efermi, 0, dosCpy, where=(EnergyCp <
#Efermi),
#alpha=0.25, facecolor='green')

#plt.plot(EnergyCs - Efermi, dostotCs, label="C-s",
#color="blue" )
#plt.fill_between(EnergyCs - Efermi, 0, dostotCs, where=(Energys <
#Efermi),
#alpha=0.25, facecolor='blue')

#plt.legend(fontsize=fontsize-2)
#plt.xlim(-12.5,5)
#plt.ylim(0,)


#ax06=plt.subplot(grid[4,0])
#plt.tick_params(axis='both', which='both',length=3, width=1.0,
#labelsize=15, right=True, top=True, direction='in')
#plt.xticks([])
#plt.ylabel("DOS(E)",fontsize=fontsize)
#plt.plot(EnergyOs - Efermi, dostotOs, label="O-s",
#color="brown" )
#plt.fill_between(EnergyOs - Efermi, 0, dostotOs, where=(EnergyOs <
#Efermi),
#alpha=0.25, facecolor='brown')


#plt.plot(EnergyOp - Efermi, dosOpz, label="O-pz",
#color="black" )
#plt.fill_between(EnergyOp - Efermi, 0, dosOpz, where=(EnergyOp <
#Efermi),
#alpha=0.25, facecolor='black')

plt.plot(EnergyOp - Efermi, dosOpx + dosCpx, label="$\pi_{x}$ character",
color="r" )
plt.fill_between(EnergyOp - Efermi, 0, dosOpx+dosCpx, where=(EnergyOp <
Efermi),
alpha=0.25, facecolor='r')

plt.plot(EnergyOp - Efermi, dosOpy+ dosCpy, label="$\pi_{y}$ character",
color="blue", linestyle="dashed" )
plt.fill_between(EnergyOp - Efermi, 0, dosOpy+dosCpy, where=(EnergyOp <
Efermi),
alpha=0.25, facecolor='blue')





plt.legend(loc='upper right',ncol=3,fontsize=fontsize-2)
plt.xlim(-12.5,5)
plt.ylim(0,)


ax06=plt.subplot(grid[0,0])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True, top=False, direction='in')
plt.xticks([])
#plt.ylabel("DOS(E)",fontsize=fontsize)
plt.plot(EnergySurd - EfermiSur, dosSurdz2, label="clean surface",
linestyle="dashed", color="green")
plt.plot(Energyd - Efermi, dosdz2, label="$d_{z^{2}}$",color="green")
plt.fill_between(Energyd - Efermi, 0, dosdz2, where=(Energyd < Efermi),
alpha=0.25, facecolor="green")
plt.legend(fontsize=fontsize-2)
plt.xlim(-12.5,5)
plt.ylim(0,)

plt.savefig('PDOS-PBETopSurfaceproj.pdf')
plt.show()



