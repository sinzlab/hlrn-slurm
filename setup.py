#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name="hlrn_slurm",
    version="0.1.4",
    description="Utility for deploying jobs on HLRN Cluster",
    author="Arne Nix",
    author_email="arnenix@gmail.com",
    packages=[],
    url="https://github.com/sinzlab/hlrn-slurm",
    scripts=["hlrn_slurm/hlrn_slurm"],
    install_requires=["jsonargparse>=4.22.1"],
)
