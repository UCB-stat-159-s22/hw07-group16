#!/bin/bash -i

mamba env create -f environment.yml -p ~/envs/hw7env
conda activate hw7env
python -m ipykernel install --user --name hw7env --display-name "IPython - hw7env"