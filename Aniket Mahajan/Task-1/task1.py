import csv
import os 
from xml.dom import minidom
import logging
logging.basicConfig(filename="unique_data.log",level=logging.DEBUG)
mobileno = ['MSISDN']
with open('sample.csv','r') as csv_file:
     csv_reader = csv.reader(csv_file, delimiter=',')
     for lines in csv_reader:
         if(lines[0] not in mobileno):
             print(lines[0]+' '+ lines[2]+' '+lines[3])
             logging.debug(lines[0]+' '+ lines[2]+' '+lines[3])
             logging.debug("data generated")
             mobileno.append(lines[0])
             
