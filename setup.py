#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name="tue-slurm",
    version="0.0.0",
    description="Utility for deploying jobs on Tue Cluster",
    author="Sinz Lab",
    author_email="info@sinzlab.com",
    packages=[],
    scripts=['bin/tue-slurm'],
    install_requires=[],
)
