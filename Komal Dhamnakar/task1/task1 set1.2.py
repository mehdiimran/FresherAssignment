#the script to accept a configuration to filter particullar service indication based on a configuration (which is provided in a external file for the python script)

import pandas as pd

df = pd.read_csv("D://sample_input.csv", header=None)

df.columns = ['MSISDN', 'operation', 'service_indication', 'TimeStamp', 'status']
# print(df)

# input from file
input = open('C:\\Users\\dhamankark\\Downloads\\indication.txt', 'r')

n = input.read()

if n == 'VM_SUBPROFILE':
    for i in df.index:
        if n == df['service_indication'][i]:
            print(df.loc[i, :])

if n == 'SMS_SUBPROFILE':
    for i in df.index:
        if n == df['service_indication'][i]:
            print(df.loc[i, :])