""" Module to provide configurations to logging acgtions """
import logging

def setup_logging()->None:
    """
    Logging setup
    """
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
