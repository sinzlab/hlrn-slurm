#!/bin/bash
export SRCDIR=$HOME/src
export WORKDIR=$SCRATCH/work
nvidia-smi
python3 -m venv $SCRATCH/env  --system-site-packages
. $SCRATCH/env/bin/activate
python3 -m pip install ipykernel
python3 -m ipykernel install --user --name=env
jupyter lab --no-browser --ip=0.0.0.0 "${@:1}"