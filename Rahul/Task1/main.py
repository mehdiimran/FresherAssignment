import pandas as pd

df = pd.read_csv("D://sample_input.csv", header=None)

df.columns = ['MSISDN', 'operation', 'service_indication', 'TimeStamp', 'status']
# print(df)

# input from file
input = open('D:\\indication.txt', 'r')

n = input.read()

if n == 'VM_SUBPROFILE':
    for i in df.index:
        if n == df['service_indication'][i]:
            print(df.loc[i, :])

if n == 'SMS_SUBPROFILE':
    for i in df.index:
        if n == df['service_indication'][i]:
            print(df.loc[i, :])