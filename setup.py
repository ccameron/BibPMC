#!/usr/bin/env python
#
# setup.py - configuration file for the bibpmc package
# author: Christopher JF Cameron
#

from setuptools import find_packages, setup

setup(
    name="bibpmc",
    version="0.0.1",
    setup_requires=["setuptools"],
    packages=find_packages(),
    install_requires=[
        "requests",
        "pybtex",
        "toolz",
        "tqdm",
    ],
    entry_points={  # Here we define the entry point for the command line tool
        "console_scripts": [
            "bibpmc=bibpmc.main:main",  # program_name is the command, and main() is the function to call
        ],
    },
    python_requires=">=3.8",
    description="BibPMC: A Python script that adds PubMed Central identifiers to BibTeX files",
    author="Christopher JF Cameron",
    author_email="30734249+ccameron@users.noreply.github.com",
    url="https://github.com/ccameron/bibpmc",
    license="BSD-3-Clause",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
