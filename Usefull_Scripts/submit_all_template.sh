#!/bin/bash

# main folder. It contains subfolders
rootFolder=???

# sequence of subfolders
list=$(seq ????? )

cd ${rootFolder} # go inside main folder

for i in ${list};do # loop over list values

	# define subfolder name. We are already inside rootFolder, so only give name. Use ${i}
	subfolder=????

	# go inside subfolder
	cd ${subfolder}
	
	# submit run_vasp.sh
  sbatch run_vasp.sh

	# go outiside one folder (i.e., back to rootFolder
	cd ..
done
