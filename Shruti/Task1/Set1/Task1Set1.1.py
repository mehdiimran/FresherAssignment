import csv
with open('E://5.Python//Datasets//sample_input.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    headings = next(reader)   
    # output list to store all rows
    Output = []
    for row in reader:
        Output.append(row[:])
    
#print(Output)

def unique(lst):
    # insert the list to the set
    list_set = set(lst)
    # convert the set to the list
    unique_list = (list(list_set))
    for x in unique_list:
        print(x)

MobNo = []
for i in range(len(Output)-1):
    MobNo.append(Output[i][0])
print("Unique Mobile nos. :")
unique(MobNo)


op_type = []
for i in range(len(Output)-1):
    op_type.append(Output[i][1])
print("Unique Operation type :.")
unique(op_type)


service_indication = []
for i in range(len(Output)-1):
    service_indication.append(Output[i][2])
print("Unique Service Indication :")
unique(service_indication)

