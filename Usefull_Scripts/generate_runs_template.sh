#!/bin/bash

# main folder. It will contain subfolders
rootFolder=???

# sequence of subfolders
list=$(seq ????? )

mkdir -p ${rootFolder}

for i in ${list};do
	# define subfolder name. Use ${i}
	subfolder=${rootFolder}/????

	# create subfolder
	mkdir -p ${subfolder}

	# copy or substitute patterns for files
  sed "s/XXX/????/g" vasp_files/INCAR.singlePointXXX > ${subfolder}/INCAR
  cp vasp_files/POTCAR.Al.pbe                          ${subfolder}/POTCAR
  cp vasp_files/POSCAR.0                               ${subfolder}/POSCAR
  cp vasp_files/KPOINTS.winner                         ${subfolder}/KPOINTS
  cp scripts/run_vasp.sh                               ${subfolder}/run_vasp.sh
done
