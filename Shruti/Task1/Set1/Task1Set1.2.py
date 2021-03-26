import csv
with open('E://5.Python//Datasets//sample_input.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    headings = next(reader)   
    # output list to store all rows
    Output = []
    for row in reader:
        Output.append(row[:])
    
#print(Output)

#input from file
input = open('E:\\5.Python\\Datasets\\indication.txt','r')

val = input.read()

# field names 
fields = ['MSISDN', 'OperationType', 'ServiceIndication', 'TimeStamp', 'Status'] 
 
if val  == 'VM_SUBPROFILE':
    service_indication = []
    for i in range(len(Output)-1):
        if Output[i][2] == "VM_SUBPROFILE":
            service_indication.append(Output[i])    
      
    with open('VM_SUBPROFILE.csv', 'w') as f:
          
        # using csv.writer method from CSV package
        write = csv.writer(f)        
        write.writerow(fields)
        write.writerows(service_indication)

elif val  == 'SMS_SUBPROFILE':
    service_indication = []
    for i in range(len(Output)-1):
        if Output[i][2] == "SMS_SUBPROFILE":
            service_indication.append(Output[i])    
      
    with open('SMS_SUBPROFILE.csv', 'w') as f:
          
        # using csv.writer method from CSV package
        write = csv.writer(f)       
        write.writerow(fields)
        write.writerows(service_indication)




    
