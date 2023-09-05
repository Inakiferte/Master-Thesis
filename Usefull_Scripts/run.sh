#!/bin/bash
#SBATCH --partition=regular
#SBATCH --job-name=single_vasp
#SBATCH --cpus-per-task=1
#SBATCH --mem=20gb
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH --reservation=esc1_22

module purge                       # purge environment inherited from modules
module load VASP/5.4.4-intel-2018a # load desidered environment
srun vasp_std                      # run vasp_std. srun applies parallelisation options set up in SLURM header
