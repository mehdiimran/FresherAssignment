from csv import reader

li1 = ['mobile number']
with open('sample_data.csv', 'r') as read_obj:
	csv_reader = reader(read_obj)
	for row in csv_reader:
		if(row[0] not in li1):
			print(row[0] + ' ' + row[1] + ' ' + row[2])
			li1.append(row[0])

	writer = csv.writer(file, quoting = csv.QUOTE_ALL, delimiter = ',')
	#writer.writerows(headers)
	writer.writerows(li2)