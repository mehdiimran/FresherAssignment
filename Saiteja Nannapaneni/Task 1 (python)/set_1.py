# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:24:54 2021

@author: tejan
"""

#first question
from csv import reader

l1 = ['MSISDN']
with open('sample_input.csv', 'r') as f:
	csv_reader = reader(f)
	for row in csv_reader:
		if(row[0] not in l1):
			print(row[0] + ' ' + row[1] + ' ' + row[2])
			l1.append(row[0])
            
            
            

#second question set1
input = open('indic.txt','r')
indication=input.read()
    
with open('sample_input.csv', 'r') as read_obj:
	csv_reader = reader(read_obj)
	for row in csv_reader:
		if(row[2] == indication):
			print(row[0] + ' '+ row[1] + ' ' + row[2] + ' '+ row[3] + ' '+ row[4])
            
            
            
            
#using pandas -------------------------------------         
            
#import pandas as pd
#data=pd.read_csv("sample_input.csv",header=None)
#data.columns =['MSISDN', 'operation type', 'service indication', 'Time Stamp','status']
#to filter the unique MSISDN
#df=data.drop_duplicates('MSISDN')




##2nd question(using pandas)
##input from console
##indication =input("Enter Service indication(VM_SUBPROFILE or SMS_SUBPROFILE):")
##print("you entered: ",indication)
##input from file
#input = open('indic.txt','r')
#n=input.read()
#if n=='VM_SUBPROFILE':
    #print(data[data['service indication']=='VM_SUBPROFILE'])
#    VM_S=data[data['service indication']=='VM_SUBPROFILE']
#    VM_S.to_csv("VM_SUBPROFILE.csv")
#elif n == "SMS_SUBPROFILE":
#    #print(data[data['service indication']=='SMS_SUBPROFILE'])
#    SMS_S=data[data['service indication']=='SMS_SUBPROFILE']
#    SMS_S.to_csv("SMS_SUBPROFILE.csv")



