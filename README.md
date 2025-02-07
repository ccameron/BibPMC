[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Python package](https://github.com/ccameron/BibPMC/actions/workflows/python-package.yml/badge.svg)](https://github.com/ccameron/BibPMC/actions/workflows/python-package.yml)

# BibPMC

`bibpmc` is a Python script that adds [PubMed Central (PMC)](https://pmc.ncbi.nlm.nih.gov/) unique identifiers (PMIDs and PMCIDs) to a [BibTeX](https://www.bibtex.org/) file, which is required for [National Institute of Health (NIH)](https://www.nih.gov/) grant applications <sup>\[[1](https://sharing.nih.gov/public-access-policy/reporting-publications-to-nih), [2](https://beckerguides.wustl.edu/nihpolicy/PMCID), [3](https://researchroadmap.mssm.edu/blog/a-guide-to-pmcid-pmid-nihms-doi-identifiers-and-the-mandatory-requirements-for-nih-supported-scientific-publications/)\]</sup>. The script uses the [digital object identifiers (DOI)](https://www.doi.org/) in a provided BibTeX file to query the [PMC API](https://pmc.ncbi.nlm.nih.gov/tools/id-converter-api/). If no DOIs are present, it will skip the query.

For validating PMC entries in a BibTeX file, see the [pmcbib](https://github.com/LelouchLamperougeVI/pmcbib) GitHub repository.

## Software requirements

1. Python v3.9+ interpreter
2. Python package dependencies described in [setup.py](https://github.com/ccameron/BibPMC/blob/main/setup.py)

## Installation

`bibpmc` installation is expected to only take a few minutes.

**<details><summary>Install using pip (recommended)</summary><p>**

```
pip install git+https://github.com/ccameron/BibPMC.git@main
```

</p></details>

**<details><summary>Install using conda</summary><p>**

1. Install [Miniforge](https://github.com/conda-forge/miniforge?tab=readme-ov-file#install) if the `conda` command is unavailable
2. Create a new Python environment and install `bibpmc` using the environment file
```
conda env create -f "https://raw.githubusercontent.com/ccameron/BibPMC/refs/heads/main/environment.yml"
```
3. Remove temporary or unused Conda files
```
conda clean --all -y
```
4. Activate the `bibpmc` Python virtual environment
```
conda activate bibpmc
```
</p></details>

To check if `bibpmc` was correctly installed, run the following command:
```
bibpmc -h
```
`bibpmc` help documentation should appear in the terminal.

## Quick start

To run `bibpmc`, use the following command:
```
bibpmc <email_address> /path/to/bibtex_file
```
Where:
- `<email_address>` is your email address (required by the PubMed Central API)
- `/path/to/bibtex_file` is the file path to the BibTeX file that you want to process

`bibpmc` will generate a new BibTeX file that includes the PMIDs and PMCIDs for the entries. 

For an example of how to incorporate the updated BibTeX file into your LaTeX project, see the [overleaf_example.zip](https://github.com/ccameron/BibPMC/blob/main/overleaf_example.zip) compressed folder.

## Command line details
```
usage: bibpmc [-h] [--include-existing] [--no-month-integer] [--out-bib out_bib] [--disable-file-logging] email in_bib

BibPMC: A Python script that adds PubMed Central identifiers to BibTeX files

positional arguments:
  email                 valid user email (required by PubMed Central API)
  in_bib                input BibTeX file path containing references

options:
  -h, --help            show this help message and exit
  --include-existing    include DOIs with existing PMID and PMCID from the BibTeX file in the PMC API query
  --no-month-integer    do not convert BibTeX month names to integers
  --out-bib out_bib     output BibTeX file path for updated references with PMIDs and PMCIDs
  --disable-file-logging
                        prevent log file creation and only print to console
```

##  Contact
[Submitting a GitHub issue](https://github.com/ccameron/BibPMC/issues) is preferred for all problems related to `bibpmc`.
