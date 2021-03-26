import os
from xml.dom import minidom
import logging
import csv

log_format = '%(asctime)s : %(message)s'
logging.basicConfig(filename="filter_service_indication.log", level=logging.DEBUG, format=log_format)

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


uniqueSubscriber()

def filterServiceIndication():
    val = raw_input("Enter service indication: ")
    val = str(val)

    list_services = []
    for i in mav_list:
        service_indication = i[2]
        if service_indication == val:
            list_services.append(i)

    print(list_services)
    logging.debug(list_services)
    logging.debug("Filtered Record Generated")
    
filterServiceIndication()