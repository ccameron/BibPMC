[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

# bibpmc

bibpmc is a Python 3 script that automatically adds [PubMed Central (PMC)](https://pmc.ncbi.nlm.nih.gov/) unique identifiers (PMIDs and PMCIDs) to a [BibTeX](https://www.bibtex.org/) file, which is required for [National Institute of Health (NIH)](https://www.nih.gov/) grant applications <sup>\[[1](https://sharing.nih.gov/public-access-policy/reporting-publications-to-nih), [2](https://beckerguides.wustl.edu/nihpolicy/PMCID), [3](https://researchroadmap.mssm.edu/blog/a-guide-to-pmcid-pmid-nihms-doi-identifiers-and-the-mandatory-requirements-for-nih-supported-scientific-publications/)\]</sup>. The script uses the [digital object identifiers (DOI)](https://www.doi.org/) in a provided BibTeX file to query the [PMC API](https://pmc.ncbi.nlm.nih.gov/tools/id-converter-api/). If no DOIs are present, it will skip the query.

For validating PMC entries in a BibTeX file, see the [pmcbib](https://github.com/LelouchLamperougeVI/pmcbib) GitHub repository.

## Software requirements

1. Python v3.11+ interpreter ([Micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) or [Miniforge](https://github.com/conda-forge/miniforge) installation recommended)
2. Python package dependencies described in setup.py

## Installation

1. [Install Miniforge](https://github.com/conda-forge/miniforge?tab=readme-ov-file#install) if the `conda` command is unavailable
2. Create a new Python virtual environment and install bibpmc dependencies:
```
conda create --name bibpmc python=3.11 conda-forge::pybtex conda-forge::requests
```
3. Remove unused or temporary Conda files:
```
conda clean --all -y
```
4. Click the "< > Code" button then "Download ZIP", unzip the file in your desired location, and rename the directory to `bibpmc`, or use `git checkout` to clone the repository:
```
git clone https://github.com/ccameron/bibpmc
```
5. Navigate the terminal to the bibpmc directory:
```
cd <install_path>/bibpmc
```

## Quick start

1. Activate the bibpmc Python virtual environment:
```
conda activate bibpmc
```
2. Run bibpmc:
```
python main.py example.bib --out example_out.bib
```

##  Contact
[Submitting a GitHub issue](https://github.com/ccameron/bibpmc/issues) is preferred for all problems related to bibpmc.
