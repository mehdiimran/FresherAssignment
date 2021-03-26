import csv
import os
from xml.dom import minidom
import logging

logging.basicConfig(filename="service_indication.log",level=logging.DEBUG)
with open('sample.csv','rb') as f:
    reader = csv.reader(f)
    for rows in reader:
        def filterservice():
            service = raw_input("Enter service name:")
            service = str(service)
            list_services = []
            person_list = []
            for i in person_list:
                service_indication = i[2]
                if service_indication == service:
                 list_services.append(i)
                print(list_services)
                logging.debug(list_services)
                logging.debug("filtered record generated")
                filterservice()