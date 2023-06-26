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

#Here plots corresponding to laser 40J/m2
#
#=======================================================
# The objective is to obtain:
#Re[\pi] = Re[\pi^{[1]}] + Re[\pi^{[2]}]
#Im[\pi] = Im[\pi^{[1]}] + Im[\pi^{[2]}]
#\Delta\omega(t) = Re[\pi(\omega,t)] - Re[\pi(\omega,0)]
#=======================================================
#
#=======================================================
#                                                      =
#vdW-DF part                                           =
#                                                      =
#=======================================================


#Read first order:

file1_vdW = "/dipc/inakiferte/vdW-DF/Pt_CO_eph/Wannier/preinterpol/results_EPW_ephinterp_k12_q12_modes_1_Titemp_Lin_80_muT/results_first_modes/results_first_order_muT.dat"
file2_vdW = "/dipc/inakiferte/vdW-DF/Pt_CO_eph/Wannier/preinterpol/results_EPW_ephinterp_k12_q12_modes_1_Titemp_Lin_80_muT/results_second_modes/results_first_order_muT.dat"
file3_vdW = "/dipc/inakiferte/vdW-DF/Pt_CO_eph/Wannier/preinterpol/results_EPW_ephinterp_k12_q12_modes_1_Titemp_Lin_80_muT/temp_F_80_chosen.in"
file_80  = "/dipc/inakiferte/vdW-DF/Pt_CO_eph/Wannier/preinterpol/TTM_results/LinPRB2008/F80Jm-2/F80.dat"
file_exp = "points-Wata80-FS.dat"
file_expl = "points-Wata80-LW.dat"

t_expl = np.loadtxt(file_expl)[:,0]
LW_exp = np.loadtxt(file_expl)[:,1]
t_exp = np.loadtxt(file_exp)[:,0]
FS_exp = np.loadtxt(file_exp)[:,1]


time_80 = np.loadtxt(file_80)[:,0] #Time for F80
Te_80   = np.loadtxt(file_80)[:,1] #Te for F80
Tl_80   = np.loadtxt(file_80)[:,2] #Tl for F80
time_vdW        = np.loadtxt(file3_vdW)[:,0] #Time in femtoseconds
Tl_vdW          = np.loadtxt(file3_vdW)[:,2] #All the lattice Temp
Te_vdW          = np.loadtxt(file1_vdW)[:,0] #All the electronic Temp.
Re_pi_supp1_vdW = np.loadtxt(file1_vdW)[:,2] #First 21 modes
Re_pi_supp2_vdW = np.loadtxt(file2_vdW)[:,2] #Second 21 modes
Im_pi_supp1_vdW = np.loadtxt(file1_vdW)[:,3] #First 21 modes
Im_pi_supp2_vdW = np.loadtxt(file2_vdW)[:,3] #Second 21 modes

#Load Raul experimental data

file_waFS="Raul-Exp/Watanabe-FS-80Jm2.dat"
file_waLW="Raul-Exp/watanabe-LW-80Jm2.dat"
file_inFS="Raul-Exp/inoue-FS-50-80Jm2.dat"

FSt_wa = np.loadtxt(file_waFS)[:,0]
FS_wa = np.loadtxt(file_waFS)[:,1]

LWt_wa = np.loadtxt(file_waLW)[:,0]
LW_wa = np.loadtxt(file_waLW)[:,1]

FSt_in = np.loadtxt(file_inFS)[:,0]
FS_in = np.loadtxt(file_inFS)[:,1]

errorFSwa = np.ones([len(FSt_wa)])
errorLWwa = np.ones([len(LWt_wa)])
errorFSin = np.ones([len(FSt_in)])

######################################


#Summ all pi values for the first order

Re_pi_firstOr_vdW = np.zeros([len(Te_vdW)]) #Define the real part of the
                                        #first order

Im_pi_firstOr_vdW = np.zeros([len(Te_vdW)]) #Define the imaginary part of
                                        #the second order

for i in range(len(Te_vdW)):
 
 Re_pi_firstOr_vdW[ i ] = Re_pi_supp1_vdW[ i ] 
 Im_pi_firstOr_vdW[ i ] = Im_pi_supp1_vdW[ i ]



#Read second order:
total_modes_vdW = 42
half_modes_vdW  = 21
Re_pi_supp3_vdW = np.zeros([len(Te_vdW)])
Re_pi_supp4_vdW = np.zeros([len(Te_vdW)])
Im_pi_supp3_vdW = np.zeros([len(Te_vdW)])
Im_pi_supp4_vdW = np.zeros([len(Te_vdW)])


#First 21 modes
for i in range(1,half_modes_vdW+1):
 file_i1_vdW = "/dipc/inakiferte/vdW-DF/Pt_CO_eph/Wannier/preinterpol/results_EPW_ephinterp_k12_q12_modes_1_Titemp_Lin_80_muT/results_first_modes/mode%.2i.dat" %i
 value_Re1_vdW = 0
 value_Im1_vdW = 0
 for j in range(len(Te_vdW)):

  value_Re1_vdW = np.loadtxt(file_i1_vdW)[j,2]
  value_Im1_vdW = np.loadtxt(file_i1_vdW)[j,3]

  Re_pi_supp3_vdW[ j ] = Re_pi_supp3_vdW[ j ] + value_Re1_vdW
  Im_pi_supp3_vdW[ j ] = Im_pi_supp3_vdW[ j ] + value_Im1_vdW

#Second 21 modes (avoid 23 and 24 modes)
#for i in range(1,2):
#  file_i2 = "results_second_modes/mode%.2i.dat" %i
#  value_Re2 = 0
#  value_Im2 = 0
#  for j in range(len(Te)):
#   value_Re2 = np.loadtxt(file_i2)[j,2]
#   value_Im2 = np.loadtxt(file_i2)[j,3]
   
#   Re_pi_supp4[ j ] = Re_pi_supp4[ j ] + value_Re2
#   Im_pi_supp4[ j ] = Im_pi_supp4[ j ] + value_Im2

for i in range(4,half_modes_vdW+1):
  file_i2_vdW = "/dipc/inakiferte/vdW-DF/Pt_CO_eph/Wannier/preinterpol/results_EPW_ephinterp_k12_q12_modes_1_Titemp_Lin_80_muT/results_second_modes/mode%.2i.dat" %i
  value_Re2_vdW = 0
  value_Im2_vdW = 0
  for j in range(len(Te_vdW)):
   value_Re2_vdW = np.loadtxt(file_i2_vdW)[j,2]
   value_Im2_vdW = np.loadtxt(file_i2_vdW)[j,3]

   Re_pi_supp4_vdW[ j ] = Re_pi_supp4_vdW[ j ] + value_Re2_vdW
   Im_pi_supp4_vdW[ j ] = Im_pi_supp4_vdW[ j ] + value_Im2_vdW


#Summ all pi values for the second order

Re_pi_secondOr_vdW = np.zeros([len(Te_vdW)]) #Define the real part of the
                                     #second order
Im_pi_secondOr_vdW = np.zeros([len(Te_vdW)]) #Define the imaginary part of
                                    #second order
for i in range(len(Te_vdW)):

 Re_pi_secondOr_vdW[ i ] = Re_pi_supp3_vdW[ i ] + Re_pi_supp4_vdW[ i ]
 Im_pi_secondOr_vdW[ i ] = Im_pi_supp3_vdW[ i ] + Im_pi_supp4_vdW[ i ]


#Obtain the values of Re[pi] and Im[pi]

Re_pi_vdW = np.zeros([len(Te_vdW)]) #Define the real part

Im_pi_vdW = np.zeros([len(Te_vdW)]) #Define the imaginary part

for i in range(len(Te_vdW)):

  Re_pi_vdW[ i ] = Re_pi_firstOr_vdW[ i ] + Re_pi_secondOr_vdW[ i ]
  Im_pi_vdW[ i ] = Im_pi_firstOr_vdW[ i ] + Im_pi_secondOr_vdW[ i ]


#Trasient frecuency shift

Frecuency_shift_vdW          = np.zeros([len(Te_vdW)])
Frecuency_shift_firstOr_vdW  = np.zeros([len(Te_vdW)])
Frecuency_shift_secondOr_vdW = np.zeros([len(Te_vdW)])
line_tot_vdW= np.zeros([len(Te_vdW)])
line_firstOr_vdW = np.zeros([len(Te_vdW)])
line_secondOr_vdW = np.zeros([len(Te_vdW)])


for i in range(len(Te_vdW)):
 
 Frecuency_shift_vdW[ i ]          = 2*(Re_pi_vdW[ i ] - Re_pi_vdW[ 0 ])
 Frecuency_shift_firstOr_vdW[ i ]  = 2*(Re_pi_firstOr_vdW[ i ] -
 Re_pi_firstOr_vdW[ 0 ])
 Frecuency_shift_secondOr_vdW[ i ] = 2*(Re_pi_secondOr_vdW[ i ] -
 Re_pi_secondOr_vdW[ 0 ])

 line_tot_vdW[ i ]          = -4.0*(Im_pi_vdW[ i ] - Im_pi_vdW[ 0 ])
 line_firstOr_vdW[ i ]  = -4.0*(Im_pi_firstOr_vdW[ i ] -
 Im_pi_firstOr_vdW[ 0 ])
 line_secondOr_vdW[ i ] = -4.0*(Im_pi_secondOr_vdW[ i ] -
 Im_pi_secondOr_vdW[ 0 ])


#=======================================================
#                                                      =
#vdW-DF part finished                                  =
#                                                      =
#=======================================================

#=======================================================
#                                                      =
#BEEF-vdW part                                         =
#                                                      =
#=======================================================


#Read first order:
file1_BEEF = "/scratch/inakiferte/CO_on_Pt/BEEF-vdW/Pt_CO_eph/CO_Top/Wannier/Wannier-Bands/interpol/results_EPW_ephinterp_k12_q12_modes_1_Titemp_Lin_80_muT/results_first_modes/results_first_order_muT.dat"
file2_BEEF = "/scratch/inakiferte/CO_on_Pt/BEEF-vdW/Pt_CO_eph/CO_Top/Wannier/Wannier-Bands/interpol/results_EPW_ephinterp_k12_q12_modes_1_Titemp_Lin_80_muT/results_second_modes/results_first_order_muT.dat"
file3_BEEF = "/scratch/inakiferte/CO_on_Pt/BEEF-vdW/Pt_CO_eph/CO_Top/Wannier/Wannier-Bands/interpol/results_EPW_ephinterp_k12_q12_modes_1_Titemp_Lin_80_muT/temp_F_80_chosen.in"

time_BEEF        = np.loadtxt(file3_BEEF)[:,0] #Time in femtoseconds
Tl_BEEF          = np.loadtxt(file3_BEEF)[:,2] #All the lattice Temp
Te_BEEF          = np.loadtxt(file1_BEEF)[:,0] #All the electronic Temp.
Re_pi_supp1_BEEF = np.loadtxt(file1_BEEF)[:,2] #First 21 modes
Re_pi_supp2_BEEF = np.loadtxt(file2_BEEF)[:,2] #Second 21 modes
Im_pi_supp1_BEEF = np.loadtxt(file1_BEEF)[:,3] #First 21 modes
Im_pi_supp2_BEEF = np.loadtxt(file2_BEEF)[:,3] #Second 21 modes

#Summ all pi values for the first order
Re_pi_firstOr_BEEF = np.zeros([len(Te_BEEF)]) #Define the real part ofthe
                                        #first order

Im_pi_firstOr_BEEF = np.zeros([len(Te_BEEF)]) #Define the imaginary part of
                                        #the second order

for i in range(len(Te_BEEF)):

  Re_pi_firstOr_BEEF[ i ] = Re_pi_supp1_BEEF[ i ]
  Im_pi_firstOr_BEEF[ i ] = Im_pi_supp1_BEEF[ i ]

#Read second order:
total_modes_BEEF = 42
half_modes_BEEF  = 21
Re_pi_supp3_BEEF = np.zeros([len(Te_BEEF)])
Re_pi_supp4_BEEF = np.zeros([len(Te_BEEF)])
Im_pi_supp3_BEEF = np.zeros([len(Te_BEEF)])
Im_pi_supp4_BEEF = np.zeros([len(Te_BEEF)])


#First 21 modes
for i in range(1,half_modes_BEEF+1):
  file_i1_BEEF = "/scratch/inakiferte/CO_on_Pt/BEEF-vdW/Pt_CO_eph/CO_Top/Wannier/Wannier-Bands/interpol/results_EPW_ephinterp_k12_q12_modes_1_Titemp_Lin_80_muT/results_first_modes/mode%.2i.dat" %i
  value_Re1_BEEF = 0
  value_Im1_BEEF = 0
  for j in range(len(Te_BEEF)):

     value_Re1_BEEF = np.loadtxt(file_i1_BEEF)[j,2]
     value_Im1_BEEF = np.loadtxt(file_i1_BEEF)[j,3]
 
     Re_pi_supp3_BEEF[ j ] = Re_pi_supp3_BEEF[ j ] + value_Re1_BEEF
     Im_pi_supp3_BEEF[ j ] = Im_pi_supp3_BEEF[ j ] + value_Im1_BEEF

#Second 21 modes (avoid 23 and 24 modes)
#for i in range(1,2):
#  file_i2 = "results_second_modes/mode%.2i.dat" %i
#  value_Re2 = 0
#  value_Im2 = 0
#  for j in range(len(Te)):
#   value_Re2 = np.loadtxt(file_i2)[j,2]
#   value_Im2 = np.loadtxt(file_i2)[j,3]
   
#   Re_pi_supp4[ j ] = Re_pi_supp4[ j ] + value_Re2
#   Im_pi_supp4[ j ] = Im_pi_supp4[ j ] + value_Im2

for i in range(4,half_modes_BEEF+1):
  file_i2_BEEF = "/scratch/inakiferte/CO_on_Pt/BEEF-vdW/Pt_CO_eph/CO_Top/Wannier/Wannier-Bands/interpol/results_EPW_ephinterp_k12_q12_modes_1_Titemp_Lin_80_muT/results_second_modes/mode%.2i.dat" %i
  value_Re2_BEEF = 0
  value_Im2_BEEF = 0
  for j in range(len(Te_BEEF)):
   value_Re2_BEEF = np.loadtxt(file_i2_BEEF)[j,2]
   value_Im2_BEEF = np.loadtxt(file_i2_BEEF)[j,3]

   Re_pi_supp4_BEEF[ j ] = Re_pi_supp4_BEEF[ j ] + value_Re2_BEEF
   Im_pi_supp4_BEEF[ j ] = Im_pi_supp4_BEEF[ j ] + value_Im2_BEEF


#Summ all pi values for the second order

Re_pi_secondOr_BEEF = np.zeros([len(Te_BEEF)]) #Define the real part of the
                                     #second order
Im_pi_secondOr_BEEF = np.zeros([len(Te_BEEF)]) #Define the imaginary part of
                                    #second order
for i in range(len(Te_BEEF)):

 Re_pi_secondOr_BEEF[ i ] = Re_pi_supp3_BEEF[ i ] + Re_pi_supp4_BEEF[ i ]
 Im_pi_secondOr_BEEF[ i ] = Im_pi_supp3_BEEF[ i ] + Im_pi_supp4_BEEF[ i ]


#Obtain the values of Re[pi] and Im[pi]

Re_pi_BEEF = np.zeros([len(Te_BEEF)]) #Define the real part

Im_pi_BEEF = np.zeros([len(Te_BEEF)]) #Define the imaginary part

for i in range(len(Te_BEEF)):

  Re_pi_BEEF[ i ] = Re_pi_firstOr_BEEF[ i ] + Re_pi_secondOr_BEEF[ i ]
  Im_pi_BEEF[ i ] = Im_pi_firstOr_BEEF[ i ] + Im_pi_secondOr_BEEF[ i ]


#Trasient frecuency shift


Frecuency_shift_BEEF          = np.zeros([len(Te_BEEF)])
Frecuency_shift_firstOr_BEEF  = np.zeros([len(Te_BEEF)])
Frecuency_shift_secondOr_BEEF = np.zeros([len(Te_BEEF)])
line_tot_BEEF= np.zeros([len(Te_BEEF)])
line_firstOr_BEEF = np.zeros([len(Te_BEEF)])
line_secondOr_BEEF = np.zeros([len(Te_BEEF)])


for i in range(len(Te_BEEF)):
 
 Frecuency_shift_BEEF[ i ]          = 2*(Re_pi_BEEF[ i ] - Re_pi_BEEF[ 0 ])
 Frecuency_shift_firstOr_BEEF[ i ]  = 2*(Re_pi_firstOr_BEEF[ i ] -
 Re_pi_firstOr_BEEF[ 0 ])
 Frecuency_shift_secondOr_BEEF[ i ] = 2*(Re_pi_secondOr_BEEF[ i ] -
 Re_pi_secondOr_BEEF[ 0 ])

 line_tot_BEEF[ i ]          = -4.0*(Im_pi_BEEF[ i ] - Im_pi_BEEF[ 0 ])
 line_firstOr_BEEF[ i ]  = -4.0*(Im_pi_firstOr_BEEF[ i ] -
 Im_pi_firstOr_BEEF[ 0 ])
 line_secondOr_BEEF[ i ] = -4.0*(Im_pi_secondOr_BEEF[ i ] -
 Im_pi_secondOr_BEEF[ 0 ])

#=======================================================
#                                                      =
#BEEF-vdW part finished                                =
#                                                      =
#=======================================================


#=======================================================
#                                                      =
#PBE part                                              =
#                                                      =
#=======================================================


#Read first order:

file1_PBE = "/dipc/inakiferte/PBE/Pt_CO_eph/Wannier/Wannier-Bands/interpol/results_EPW_ephinterp_k12_q12_modes_1_Titemp_Lin_80_muT/results_first_modes/results_first_order_muT.dat"
file2_PBE = "/dipc/inakiferte/PBE/Pt_CO_eph/Wannier/Wannier-Bands/interpol/results_EPW_ephinterp_k12_q12_modes_1_Titemp_Lin_80_muT/results_second_modes/results_first_order_muT.dat"
file3_PBE = "/dipc/inakiferte/PBE/Pt_CO_eph/Wannier/Wannier-Bands/interpol/results_EPW_ephinterp_k12_q12_modes_1_Titemp_Lin_80_muT/temp_F_80_chosen.in"

time_PBE        = np.loadtxt(file3_PBE)[:,0] #Time in femtoseconds
Tl_PBE          = np.loadtxt(file3_PBE)[:,2] #All the lattice Temp
Te_PBE          = np.loadtxt(file1_PBE)[:,0] #All the electronic Temp.
Re_pi_supp1_PBE = np.loadtxt(file1_PBE)[:,2] #First 21 modes
Re_pi_supp2_PBE = np.loadtxt(file2_PBE)[:,2] #Second 21 modes
Im_pi_supp1_PBE = np.loadtxt(file1_PBE)[:,3] #First 21 modes
Im_pi_supp2_PBE = np.loadtxt(file2_PBE)[:,3] #Second 21 modes



#Summ all pi values for the first order

Re_pi_firstOr_PBE = np.zeros([len(Te_PBE)]) #Define the real part of the
                                        #first order

Im_pi_firstOr_PBE = np.zeros([len(Te_PBE)]) #Define the imaginary part of
                                        #the second order

for i in range(len(Te_PBE)):
 
 Re_pi_firstOr_PBE[ i ] = Re_pi_supp1_PBE[ i ] 
 Im_pi_firstOr_PBE[ i ] = Im_pi_supp1_PBE[ i ]



#Read second order:
total_modes_PBE = 42
half_modes_PBE  = 21
Re_pi_supp3_PBE = np.zeros([len(Te_PBE)])
Re_pi_supp4_PBE = np.zeros([len(Te_PBE)])
Im_pi_supp3_PBE = np.zeros([len(Te_PBE)])
Im_pi_supp4_PBE = np.zeros([len(Te_PBE)])


#First 21 modes
for i in range(1,half_modes_PBE+1):
 file_i1_PBE = "/dipc/inakiferte/PBE/Pt_CO_eph/Wannier/Wannier-Bands/interpol/results_EPW_ephinterp_k12_q12_modes_1_Titemp_Lin_80_muT/results_first_modes/mode%.2i.dat" %i
 value_Re1_PBE = 0
 value_Im1_PBE = 0
 for j in range(len(Te_PBE)):

  value_Re1_PBE = np.loadtxt(file_i1_PBE)[j,2]
  value_Im1_PBE = np.loadtxt(file_i1_PBE)[j,3]

  Re_pi_supp3_PBE[ j ] = Re_pi_supp3_PBE[ j ] + value_Re1_PBE
  Im_pi_supp3_PBE[ j ] = Im_pi_supp3_PBE[ j ] + value_Im1_PBE

#Second 21 modes (avoid 23 and 24 modes)
#for i in range(1,2):
#  file_i2 = "results_second_modes/mode%.2i.dat" %i
#  value_Re2 = 0
#  value_Im2 = 0
#  for j in range(len(Te)):
#   value_Re2 = np.loadtxt(file_i2)[j,2]
#   value_Im2 = np.loadtxt(file_i2)[j,3]
   
#   Re_pi_supp4[ j ] = Re_pi_supp4[ j ] + value_Re2
#   Im_pi_supp4[ j ] = Im_pi_supp4[ j ] + value_Im2

for i in range(4,half_modes_PBE+1):
  file_i2_PBE = "/dipc/inakiferte/PBE/Pt_CO_eph/Wannier/Wannier-Bands/interpol/results_EPW_ephinterp_k12_q12_modes_1_Titemp_Lin_80_muT/results_second_modes/mode%.2i.dat" %i
  value_Re2_PBE = 0
  value_Im2_PBE = 0
  for j in range(len(Te_PBE)):
   value_Re2_PBE = np.loadtxt(file_i2_PBE)[j,2]
   value_Im2_PBE = np.loadtxt(file_i2_PBE)[j,3]

   Re_pi_supp4_PBE[ j ] = Re_pi_supp4_PBE[ j ] + value_Re2_PBE
   Im_pi_supp4_PBE[ j ] = Im_pi_supp4_PBE[ j ] + value_Im2_PBE


#Summ all pi values for the second order

Re_pi_secondOr_PBE = np.zeros([len(Te_PBE)]) #Define the real part of the
                                     #second order
Im_pi_secondOr_PBE = np.zeros([len(Te_PBE)]) #Define the imaginary part of
                                    #second order
for i in range(len(Te_PBE)):

 Re_pi_secondOr_PBE[ i ] = Re_pi_supp3_PBE[ i ] + Re_pi_supp4_PBE[ i ]
 Im_pi_secondOr_PBE[ i ] = Im_pi_supp3_PBE[ i ] + Im_pi_supp4_PBE[ i ]


#Obtain the values of Re[pi] and Im[pi]

Re_pi_PBE = np.zeros([len(Te_PBE)]) #Define the real part

Im_pi_PBE = np.zeros([len(Te_PBE)]) #Define the imaginary part

for i in range(len(Te_PBE)):

  Re_pi_PBE[ i ] = Re_pi_firstOr_PBE[ i ] + Re_pi_secondOr_PBE[ i ]
  Im_pi_PBE[ i ] = Im_pi_firstOr_PBE[ i ] + Im_pi_secondOr_PBE[ i ]

#Trasient frecuency shift

Frecuency_shift_PBE          = np.zeros([len(Te_PBE)])
Frecuency_shift_firstOr_PBE  = np.zeros([len(Te_PBE)])
Frecuency_shift_secondOr_PBE = np.zeros([len(Te_PBE)])
line_tot_PBE= np.zeros([len(Te_PBE)])
line_firstOr_PBE = np.zeros([len(Te_PBE)])
line_secondOr_PBE = np.zeros([len(Te_PBE)])


for i in range(len(Te_PBE)):
 
 Frecuency_shift_PBE[ i ]          = 2*(Re_pi_PBE[ i ] - Re_pi_PBE[ 0 ])
 Frecuency_shift_firstOr_PBE[ i ]  = 2*(Re_pi_firstOr_PBE[ i ] -
 Re_pi_firstOr_PBE[ 0 ])
 Frecuency_shift_secondOr_PBE[ i ] = 2*(Re_pi_secondOr_PBE[ i ] -
 Re_pi_secondOr_PBE[ 0 ])

 line_tot_PBE[ i ]          = -4.0*(Im_pi_PBE[ i ] - Im_pi_PBE[ 0 ])
 line_firstOr_PBE[ i ]  = -4.0*(Im_pi_firstOr_PBE[ i ] -
 Im_pi_firstOr_PBE[ 0 ])
 line_secondOr_PBE[ i ] = -4.0*(Im_pi_secondOr_PBE[ i ] -
 Im_pi_secondOr_PBE[ 0 ])


#=======================================================
#                                                      =
#PBE part finished                                     =
#                                                      =
#=======================================================



#Plot

fontsize=15


plt.figure(figsize = (12,6))
grid = plt.GridSpec(3, 1, hspace = 0.0)


ax01=plt.subplot(grid[0])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True,top=True, direction='out')
plt.ylabel("$T~(10^{3}K)$",fontsize=fontsize)
plt.xlabel("t (ps)",fontsize=fontsize)
plt.plot(time_80*10**(-3), Te_80*10**(-3), label='$T_{e}$')
plt.plot(time_80*10**(-3), Tl_80*10**(-3), label='$T_{l}$')
plt.xlim(-1.5,10)
#plt.legend()
plt.text(-1, 4.0, '(a)', ha='center', va='bottom', fontsize=fontsize)

ax02=plt.subplot(grid[1])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True,top=False, direction='out')
plt.ylabel("$\Delta\gamma(cm^{-1})$",fontsize=fontsize)
plt.xlabel("t (ps)",fontsize=fontsize)
plt.plot(time_vdW*10**(-3), line_tot_PBE, color= 'blue', label='PBE',
linewidth=1,marker='s',markersize=fontsize-12)
#plt.plot(time_vdW*10**(-3), line_tot_vdW, color='darkorange',
#label='vdW-DF', linewidth=1,marker='s',markersize=fontsize-12)
plt.plot(time_vdW*10**(-3), line_tot_BEEF, color='green', label='BEEF',
linewidth=1,marker='s',markersize=fontsize-12)
plt.plot(time_vdW*10**(-3), line_firstOr_BEEF,
color='green',linestyle='dashed', label='First Order',
linewidth=1,marker='s',markersize=fontsize-12)
#plt.plot(t_expl+0.3, LW_exp, color='red', label='Experiment',
#linewidth=1,marker='s',markersize=fontsize-12)

#Raul exp

#plt.plot(LWt_wa, LW_wa, color='red', label='Watanabe',
#linewidth=1,marker='s',markersize=fontsize-12)

plt.errorbar(LWt_wa, LW_wa-LW_wa[0], yerr=errorLWwa, color='red',
label='Wata', linewidth=1,marker='o',markersize=fontsize-12, capsize=4,
linestyle='')

#########

plt.xlim(-1.5,10)
plt.legend(fontsize=fontsize-2)
plt.text(-1, 5.0, '(b)', ha='center', va='bottom', fontsize=fontsize)
frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])

ax03=plt.subplot(grid[2])
plt.tick_params(axis='both', which='both',length=3, width=1.0,
labelsize=15, right=True,top=False, direction='out')
plt.ylabel("$\Delta\omega~(cm^{-1})$",fontsize=fontsize)
plt.xlabel("t (ps)",fontsize=fontsize)
plt.plot(time_vdW*10**(-3), Frecuency_shift_PBE, color= 'blue',
label='PBE', linewidth=1,marker='s',markersize=fontsize-12)
#plt.plot(time_vdW*10**(-3), Frecuency_shift_vdW, color='darkorange',
#label='vdW-DF', linewidth=1,marker='s',markersize=fontsize-12)
plt.plot(time_vdW*10**(-3), Frecuency_shift_BEEF,color='green',
label='BEEF-vdW', linewidth=1,marker='s',markersize=fontsize-12)
plt.plot(time_vdW*10**(-3),
Frecuency_shift_firstOr_BEEF, linestyle='dashed', color='green',
label='First Order', linewidth=1,marker='s',markersize=fontsize-12)
#plt.plot(t_exp+0.3, FS_exp-FS_exp[0],color='red',
#label='Experiment', linewidth=1,marker='o',markersize=fontsize-12)

#Raul exp

plt.errorbar(FSt_wa, FS_wa-FS_wa[0], yerr=errorFSwa, color='orange',
label='Wata', linewidth=1,marker='o',markersize=fontsize-12, capsize=4,
linestyle='')

#plt.plot(FSt_wa, FS_wa-FS_wa[0],color='orange',
#label='Wata', linewidth=1,marker='o',markersize=fontsize-12)

#plt.plot(FSt_in+0.3, FS_in-FS_in[0],color='purple',
#label='Inoue + 0.3 ps', linewidth=1,marker='o',markersize=fontsize-12)

plt.errorbar(FSt_in, FS_in-FS_in[0], yerr=errorFSin, color='purple',
label='Inoue', linewidth=1,marker='o',markersize=fontsize-12, capsize=4,
linestyle='')

#########################33

plt.legend(fontsize=fontsize-2)
plt.xlim(-1.5,10)
plt.text(-1, -5, '(c)', ha='center', va='bottom', fontsize=fontsize)
#frame1 = plt.gca()
#frame1.axes.xaxis.set_ticklabels([])


plt.savefig('Functionals-top-Lin-80Delta.pdf')
plt.show()

