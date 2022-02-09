#!/bin/bash
export SRCDIR=$HOME/projects
export WORKDIR=$SCRATCH/work
nvidia-smi
python3 -m venv $1/env  --system-site-packages
. $1/env/bin/activate
python3 bias_transfer_recipes/main.py "${@:1}"
