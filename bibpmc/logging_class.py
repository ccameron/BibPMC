#!/usr/bin/env python
#
# logging_class.py - set up logging
# author: Christopher JF Cameron
#

import logging
import os


class LoggingClass:
    """
    Logging class for BibPMC

    Attributes:
        name (str): The name of the logger
        log_file (str): The path to the output log file
        logger (logging.Logger): The logger object

    Methods:
        __init__(): Initialize the logger
        get_logger(): Get the logger object
        remove_file_handler(): Remove the file handler from the logger
    """

    name = "BibPMC"
    log_file = os.path.join(os.getcwd(), f"{name}.log")

    def __init__(self):
        # initialize
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)
        logger_fmt = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # set stdout stream handler
        log_stdout = logging.StreamHandler()
        log_stdout.setFormatter(logger_fmt)
        log_stdout.setLevel(logging.INFO)

        # set file handler
        log_file = logging.FileHandler(self.log_file)
        log_file.setLevel(logging.DEBUG)
        log_file.setFormatter(logger_fmt)

        # add handlers
        self.logger.addHandler(log_file)
        self.logger.addHandler(log_stdout)

        del logger_fmt, log_stdout, log_file

    def get_logger(self):
        """
        Get the logger object

        Args:
            None

        Returns:
            logging.Logger: The logger object
        """
        return self.logger

    def remove_file_handler(self) -> None:
        """
        Remove the file handler from the logger

        Args:
            None

        Returns:
            None
        """
        # remove file handler from logger
        for handler in self.logger.handlers:
            if isinstance(handler, logging.FileHandler):
                self.logger.removeHandler(handler)
                self.logger.info("removed file handler from logger")
                break

        # delete log file if it exists
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
            self.logger.info(f"removed log file: {self.log_file}")


# expose logger object and class instance
log_instance = LoggingClass()
logger = log_instance.get_logger()
