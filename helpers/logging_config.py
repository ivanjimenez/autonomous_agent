""" Module to provide configurations to logging acgtions """
import logging
from config import LOG_FILE_PATH


def setup_logging()->None:
    """
    Logging setup
    """
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def setup_logging_file():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=LOG_FILE_PATH,
        filemode='w'
    )
