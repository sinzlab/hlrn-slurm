#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name="hlrn-slurm",
    version="0.0.0",
    description="Utility for deploying jobs on HLRN Cluster",
    author="Arne Nix",
    author_email="info@sinzlab.com",
    packages=[],
    scripts=['bin/hlrn-slurm'],
    install_requires=[],
)
