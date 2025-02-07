#!/usr/bin/env python
#
# args.py - functions for command line argument parsing
# author: Christopher JF Cameron
#

import argparse
import os
import re
import sys

from bibpmc.logging_class import logger, log_instance


def is_valid_email(email: str) -> bool:
    """
    Check if email is valid

    Args:
        email (str): Email address to validate

    Returns:
        bool: True if email is valid, False otherwise

    """
    return bool(re.search(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email))


def parse_args() -> argparse.Namespace:
    """
    Parse command line arguments

    Args:
        None

    Returns:
        argparse.Namespace: Parsed command line arguments
    """
    parser = argparse.ArgumentParser(
        description="BibPMC: A Python package that adds PubMed Central identifiers to BibTeX files"
    )
    parser.add_argument(
        "email",
        metavar="email",
        type=str,
        help="valid user email (required by PubMed Central API)",
    )
    parser.add_argument(
        "in_bib",
        metavar="in_bib",
        type=str,
        help="input BibTeX file path containing references",
    )
    parser.add_argument(
        "--include-existing",
        action="store_true",
        help="include DOIs with existing PMID and PMCID from the BibTeX file in the PMC API query",
    )
    parser.add_argument(
        "--no-month-integer",
        action="store_true",
        help="do not convert BibTeX month names to integers",
    )
    parser.add_argument(
        "--out-bib",
        metavar="out_bib",
        type=str,
        help="output BibTeX file path for updated references with PMIDs and PMCIDs",
    )
    parser.add_argument(
        "--disable-file-logging",
        action="store_true",
        help="prevent log file creation and only print to console",
    )
    args = parser.parse_args()

    # validate command line arguments
    if not os.path.exists(args.in_bib):
        logger.error(f"Error - {args.in_bib} does not exist")
        sys.exit(-1)
    if not is_valid_email(args.email):
        logger.error(f"Error - {args.email} is not a valid email address")
        sys.exit(-1)
    args.out_bib = (
        args.out_bib
        if args.out_bib
        else f"{os.path.splitext(args.in_bib)[0]}_BibPMC.bib"
    )

    logger.info(
        "BibPMC: A Python script that adds PubMed Central identifiers to BibTeX files"
    )
    logger.info("command line arguments:")
    logger.info(f"\tinput BibTeX file: {args.in_bib}")
    logger.info(f"\toutput BibTeX file: {args.out_bib}")
    logger.info(f"\tuser email: {args.email}")
    logger.info(f"\tinclude existing DOIs: {args.include_existing}")
    logger.info(f"\tconvert month names to integers: {not args.no_month_integer}")

    if args.disable_file_logging:
        logger.info("Warning - preventing log files and only printing to console")
        log_instance.remove_file_handler()

    return args
