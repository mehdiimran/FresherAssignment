import numpy as np
import pandas as pd

df = pd.read_csv("E://5.Python//Datasets//sample_input.csv",header=None)

df.columns = ['MSISDN', 'OperationType', 'ServiceIndication', 'TimeStamp', 'Status']
#print(df)

#input from file
input = open('E:\\5.Python\\Datasets\\indication.txt','r')

val = input.read()


if val  == 'VM_SUBPROFILE':
    VM_Subprofile=df[df['ServiceIndication']=='VM_SUBPROFILE']
    VM_Subprofile.to_csv("VM_SUBPROFILE.csv")
    
elif val  == "SMS_SUBPROFILE":
    #print(data[data['service_indication']=='VM_SUBPROFILE'])
    SMS_Subprofile=df[df['ServiceIndication']=='SMS_SUBPROFILE']
    SMS_Subprofile.to_csv("SMS_SUBPROFILE.csv")

