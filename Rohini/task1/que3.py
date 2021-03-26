import csv


f = open('output_data.csv')
csv_f = csv.reader(f)   
data = []

for row in csv_f: 
	data.append(row)
f.close()

def convert_row(row):
	return 

with open('output.xml', 'w') as f: f.write('\n'.join([convert_row(row) for row in data]))