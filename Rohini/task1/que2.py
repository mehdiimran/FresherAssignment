

from csv import reader

type_service = input("Enter service name(VM/SMS): ")
type_service = type_service.lower()
if(type_service == 'vm'):
	type_service = 'VM_SUBPROFILE'
elif(type_service == 'sms'):
	type_service =  'SMS_SUBPROFILE'
else:
	print("Invalid input")
	type_service = lower(input("Enter service name(VM/SMS): "))
with open('sample_data.csv', 'r') as read_obj:
	csv_reader = reader(read_obj)
	for row in csv_reader:
		if(row[2] == type_service):
			print(row[0] + ' '+ row[1] + ' ' + row[2] + ' '+ row[3] + ' '+ row[4])