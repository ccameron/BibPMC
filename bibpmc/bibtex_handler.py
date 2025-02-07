#!/usr/bin/env python
#
# bibtex_handler.py - functions for handling BibTeX entries
# author: Christopher JF Cameron
#

import sys

from bibpmc.logging_class import logger
from pybtex.database import parse_file  # type: ignore

MTH_DICT = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "11": 11,
    "12": 12,
}


def get_doi_from_bib(data: dict, include_existing: bool = False) -> set:
    """
    Extract DOIs from BibTeX entries

    Args:
        data (dict): BibTeX entries
        include_existing (bool): Include DOIs with existing PMCID/PMID in the PMC API query

    Returns:
        doi_set (set): Set of DOIs
    """
    logger.info("extracting DOIs from BibTeX entries")
    doi_set = set([])
    for entry in data.entries.values():
        # extract DOI, PMCID, and PMID from BibTeX entry
        doi = entry.fields.get("doi")
        pmcid = entry.fields.get("pmcid")
        pmid = entry.fields.get("pmid")

        if doi in doi_set and doi is not None:
            # None is most likely a BibTex entry without a DOI
            logger.warning(f"Warning - duplicate DOI found: {doi}")
        # add DOI to set if it does not exist or include_existing is True
        if include_existing or (pmcid is None and pmid is None):
            doi_set.add(doi)
    del entry, doi
    # remove None values from set
    doi_set.discard(None)

    if not len(doi_set) > 0:
        logger.error(f"Error - No DOIs found in BibTeX file")
        sys.exit(-1)

    return doi_set


def read_bib_file(in_file: str) -> dict:
    """
    Read BibTeX file into memory

    Args:
        in_file (str): Path to BibTeX file

    Returns:
        dict: BibTeX entries
    """
    logger.info(f"reading BibTeX file: {in_file}")
    return parse_file(in_file)


def update_bib_entries(data: dict, id_dict: dict, month_int: bool = True) -> None:
    """
    Update BibTeX entries with PMIDs and PMCIDs

    Args:
        data (dict): BibTeX entries
        id_dict (dict): Dictionary of DOIs with PMID and PMCID
        month_int (bool): Convert BibTeX month strings to integers

    Returns:
        None
    """
    logger.info("updating BibTeX entries with PMIDs and PMCIDs")
    # update BibTeX entries with PMIDs and PMCIDs
    for entry_key, entry in data.entries.items():

        # add PMIDs and PMCIDs to BibTeX entries
        doi = entry.fields.get("doi")
        try:
            entry.fields["pmcid"] = id_dict[doi]["pmcid"]
            entry.fields["pmid"] = id_dict[doi]["pmid"]
        except KeyError:
            pass
        # update month field
        if month_int:
            month = entry.fields.get("month")
            if month is not None:
                entry.fields["month"] = str(MTH_DICT[month.strip().lower()])
    del entry_key, entry, doi


def write_bib(data, out_bib: str) -> None:
    """
    Write updated BibTeX entries to file

    Args:
        data (dict): BibTeX entries
        out_bib (str): Output BibTeX file path

    Returns:
        None
    """
    logger.info(f"writing updated BibTeX entries to {out_bib}")
    with open(out_bib, "wt") as o:
        data.to_file(o)
