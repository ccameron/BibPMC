#!/usr/bin/env python
#
# test_help.py - test BibPMC installation using the -h flag
# author: Christopher JF Cameron
#

import subprocess


def test_help_command() -> None:
    """
    Test the help command

    Args:
        None

    Returns:
        None
    """
    result = subprocess.run(["bibpmc", "-h"], capture_output=True, text=True)
    # Check if the command ran successfully
    assert result.returncode == 0, f"help command failed with error: {result.stderr}"

    # Check if the help message contains the expected content
    assert "usage" in result.stdout.lower(), "help documentation was not displayed"
    assert "--help" in result.stdout.lower(), "-h option not recognized"


test_help_command()
