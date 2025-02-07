#!/usr/bin/env python
#
# main.py - add PMIDs and PMCIDs to a BibTeX file (requires DOIs for BibTeX entries)
# author: Christopher JF Cameron
#

import os

from bibpmc.args import parse_args
from bibpmc.bibtex_handler import (
    get_doi_from_bib,
    read_bib_file,
    update_bib_entries,
    write_bib,
)
from bibpmc.pmc_api import get_pmcid_by_doi


def main() -> None:
    """
    Main function for BibPMC

    Args:
        None

    Returns:
        None
    """
    # parse command line arguments
    args = parse_args()

    # read BibTeX file into memory
    data = read_bib_file(args.in_bib)

    # iterate over BibTeX entries and extract DOIs
    dois = get_doi_from_bib(data, args.include_existing)

    # query PMC Any ID Converter API
    id_dict = get_pmcid_by_doi(
        dois, args.email, os.path.dirname(args.out_bib), args.disable_file_logging
    )

    # update BibTeX entries
    update_bib_entries(data, id_dict, args.no_month_integer)

    # write updated BibTeX entries to file
    write_bib(data, args.out_bib)


if __name__ == "__main__":
    main()
