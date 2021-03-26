
import numpy as np
import pandas as pd

df = pd.read_csv("E://5.Python//Datasets//sample_input.csv",header=None)

#1. python script to filter the unique MSISDN(mobile number- first column data in the list),
# operation type (ADD/ DELETE/ MODIFY) and service indication (VM_SUBPROFILE/SMS_SUBPROFILE) 

print(df.iloc[:,0].unique())
#[11234567893 11234567894 11234567895 11234567897 11234567890]

print(df.iloc[:,1].unique())
#['ADD' 'DELETE']

print(df.iloc[:,2].unique())
#['VM_SUBPROFILE' 'SMS_SUBPROFILE']



