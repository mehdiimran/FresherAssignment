import csv
import pandas as pd

df = pd.read_csv("sample_input.csv")
# read specific columns of csv file using Pandas
#df = pd.read_csv("sample_input.csv", usecols = ['Phone_no'])
#print(df)
record = pd.read_csv("sample_input.csv")
print(pd.unique(record['Phone_no']))
print(df)
column_values = df [["Phone_no" , "Operation_type" , "Service_indication"]].values.ravel()
unique_values =  pd.unique(column_values)
print(unique_values