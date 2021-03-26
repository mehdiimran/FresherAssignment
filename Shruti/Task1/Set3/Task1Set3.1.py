# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 12:49:28 2021

@author: Maooli
"""

import logging
log_format = '%(asctime)s : %(message)s'
logging.basicConfig(filename="log1.log", level=logging.DEBUG, format=log_format)
logging.debug("Reading Record of Csv file successfully done") 