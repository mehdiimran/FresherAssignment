import pandas as pd
import os
from xml.dom import minidom
import logging

logging.basicConfig(filename="unique_record.log", level=logging.DEBUG)
data_file = pd.read_csv("sample_input.csv", usecols=[0, 1, 2])

result = pd.read_csv('sample_input.csv')
mav_list = [list(i) for i in result.values]

list_subs = []

def uniqueSubscriber():
    for i in mav_list:
        flag = 1
        for j in list_subs:
            flag = 1
            if j[0] == i[0]:
                flag = 0
                break
        if flag:
            list_subs.append(i[:5])

    for i in list_subs:
        print(i)
        logging.debug(i)
    logging.debug("Unique Record Generated")


uniqueSubscriber()