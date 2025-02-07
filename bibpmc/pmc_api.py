#!/usr/bin/env python
#
# pmc_api.py - functions for querying the PubMed Central API
# author: Christopher JF Cameron
#

import os
import requests  # type: ignore
import time
import xml.etree.ElementTree as ET

from bibpmc.logging_class import logger
from toolz import partition_all  # type: ignore
from tqdm import tqdm  # type: ignore

QUERY_SIZE = 128
PMC_ANY_ID_CONVERTER_URL = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"
# src - https://pmc.ncbi.nlm.nih.gov/tools/id-converter-api/


def get_pmcid_by_doi(
    dois: set, email: str, out_dir: str = None, disable_file_logging: bool = False
) -> dict:
    """
    Returns dictionary of PM(C)IDs for DOIs

    Args:
        dois (set): Set of DOIs
        email (str): User email address
        out_dir (str): Output directory for response XML file
        disable_file_logging (bool): Prevent XML file output (default: False)

    Returns:
        id_dict (dict): Dictionary of DOIs (keys) with PMID and PMcID
    """
    # src - https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/
    logger.info("querying PubMed Central API for PMIDs and PMCIDs")
    out_file = os.path.join(
        out_dir if out_dir else os.getcwd(),
        f"pmc_query_{time.strftime('%Y%m%d_%H%M', time.localtime())}.xml",
    )
    logger.info(f"writing PMC API response to {out_file}")

    chunks = list(partition_all(QUERY_SIZE, dois))
    for chunk in tqdm(
        chunks,
        desc="Querying PubMed Central API",
        unit=" 128-DOI chunk",
    ):
        ids = ",".join(chunk)
        id_dict = {}
        pmc_url = f"{PMC_ANY_ID_CONVERTER_URL}?ids={ids}&tool=BibPMC&email={email}"
        response = requests.get(pmc_url)
        if response.status_code == 200:
            root = ET.fromstring(response.content)

            if not disable_file_logging:
                # save response (XML file) to storage
                if os.path.exists(out_file):
                    tree = ET.parse(out_file)
                    root_old = tree.getroot()
                    root_old.extend(root)
                else:
                    tree = ET.ElementTree(root)
                tree.write(out_file, encoding="utf-8", xml_declaration=True)
                del tree

            # extract PMIDs and PMCIDs from response
            for record in root.iter("record"):
                doi = record.get("doi")
                pmcid = record.get("pmcid")
                pmid = record.get("pmid")
                if doi and pmcid is not None and pmid is not None:
                    id_dict[doi] = {"pmcid": pmcid, "pmid": pmid}
            del root, record, doi, pmcid, pmid
        else:
            logger.error(
                f"Error - PMC API request failed with status code: {response.status_code}"
            )
    del chunk, ids, pmc_url, response

    return id_dict
