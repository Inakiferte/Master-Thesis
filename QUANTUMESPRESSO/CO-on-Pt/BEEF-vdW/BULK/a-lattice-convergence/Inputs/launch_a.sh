#!/bin/bash

# Begin relaxation loop

# Generic in_file to modify
generic_name_file="Pt.scf"
prefix="Ptbulk"


for z in 7.571 7.572 7.573 7.574 7.576 7.577 7.578 7.579
# loop for i in {min..max..increment} 
#for i in {0..10..2} 
do

name_file="${generic_name_file}_$z"

cp ${generic_name_file}.in ${name_file}.in 
 
 ZZ=$(echo "$z" |bc -l)
 sed -i "s/ZZ/${ZZ}/g" ${name_file}.in

# creating job
name="scf_$z"
nnodes=3
cat >>job_${z}<<EOF
#!/bin/bash
#SBATCH --partition=95g
#SBATCH --time 24:00:00
#SBATCH --nodes=$nnodes
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=1
#SBATCH --mem=8000
#SBATCH --job-name=$name
#SBATCH --output=$name.out
#SBATCH --error=$name.err




##############
# Load modules
##############

echo 'loading modules...'
module load intel/2016a
PWX=/home/tetenoire/QESPRESSO/qe-7.1/bin/pw.x
echo 'module load finished'


# In and out files

in_file="${name_file}.in"
out_file="${name_file}.out"

echo 'in_file out_file'
echo \${in_file} \${out_file}
echo


# We create the folders that we need 

# This the directory from where we launch the calculation
DIR=$(pwd)

echo \$DIR

# Directory where the files that we need for the calcualtion are
PREDD="\$DIR"
# Directory where results will be copied
DD="\${DIR}/results_a_$z"

# We create it if it does not exist
if [ -d \${DD} ]
 then
  chmod -R 700 \${DD}
 else
  mkdir -p \${DD}
  chmod -R 700 \${DD}
fi


echo \${PREDD}
echo \${DD}
cd \${PREDD}

# We print the name of the node where the calculation is running
# to the file node_name
hostname > \${DD}/node_name_${z}

# working directory
karp="CO_on_Pt/BEEF-vdW/BULK/ecut_$z"
WD="/scratch/\${USER}/\${karp}"

# We create it if it doesn't exist
# if it exist remove and create it again
if [ -d \${WD} ]
 then
  rm -rf \${WD}
  mkdir -p \${WD}
  chmod -R 700 \${WD}
 else
  mkdir -p \${WD}
  chmod -R 700 \${WD}
fi
echo \${WD}
#copy from files from PREDD to WD

cp -r \${PREDD}/pseudo \${WD}/
cp \${PREDD}/\${in_file}   \${WD}/

# Enter working directory and start the calculation
cd \${WD}


export OMP_NUM_THREADS=\${SLURM_NTASKS_PER_NODE}

mpirun  -np 24 \${PWX}  -nk 24 -nb 1 -nt 1 -nd 1 < \${in_file}  > \${out_file} 

echo "calculation finished"

# copy results to results directory
# and remove thrash


cp \${out_file} \${DD}/
#cp -r \${PREFIX}* \${DD}/

cp * \${DD}/

rm  -r \${WD}/tmp



EOF

#sending jobs


sbatch job_$z
rm job_$z

#end loops

done
