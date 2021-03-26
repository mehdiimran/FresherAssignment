# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:28:44 2021

@author: tejan
"""

#set2  both the questions based on size




#limiting with the batch size 

import csv
print("begin writing xml")

n=input("enter the batch size")

#reader=csv.reader(open("sample_input.csv",'r'),delimiter=',')
reader=csv.reader(open("VM_SUBPROFILE.csv",'r'),delimiter=',')
next(reader)

#open xml file
f=open('VM_SUB(limited).xml','w')
#f=open('x.xml','w')

#xml declaration
f.write('<?xml version="1.0" encoding="UTF-8"?>')

#xml root element
f.write('<Audit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="schema.xsd">')

count=0
for row in reader:
    #xml child element
    f.write('    '+'<auditSubscribers>')
    f.write('    '+'<MSISDN>'+row[0]+'</MSISDN>')
    f.write('    '+'<OperationType>'+row[1]+'</OperationType>')
    f.write('    '+'<ServiceIndication>'+row[2]+'</ServiceIndication>')
    f.write('    '+'</auditSubscribers>')
    count=count+1
    if count == n :
        break
        
#xml end root element
f.write('</Audit>')
f.close()
print("finished writing xml")
