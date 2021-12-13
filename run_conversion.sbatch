#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=64G
#SBATCH -p small
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=mhtoin@utu.fi
#SBATCH -t 48:00:00
#SBATCH --ntasks-per-node=1
#SBATCH --account=Project_2002026
#SBATCH -o logs/%j.out
#SBATCH -e logs/%j.err

source transformers3.4/bin/activate

export INPUT=$1

srun python convert_to_tsv.py --lang $1