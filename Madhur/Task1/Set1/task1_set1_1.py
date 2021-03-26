import os
from xml.dom import minidom
import logging
import csv

logging.basicConfig(filename="unique_record.log", level=logging.DEBUG)

mav_list = []
list_subs = []

with open('sample_input.csv', 'rb') as f:
    reader = csv.reader(f)
    for rows in reader:
        mav_list.append(rows)


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