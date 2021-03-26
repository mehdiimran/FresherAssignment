import logging
log_format = '%(asctime)s : %(message)s'
logging.basicConfig(filename="test.log", level=logging.DEBUG, format=log_format)
logging.debug("Reading Record of Csv file successfully done")