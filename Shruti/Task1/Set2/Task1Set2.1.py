import csv

print('Begin writing xml')

reader = csv.reader(open('C:\\Users\\Maooli\\Documents\\VM_SUBPROFILE.csv','r'), delimiter=',')

f = open('C:\\Users\\Maooli\\Documents\\VM_SUBPROFILE.xml', 'w')


f.write('<?xml version="1.0" encoding="UTF-8"?>')

# xml root element

f.write('<Audit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="schema.xsd">')

for row in reader:
    # xml child element
    f.write('    ' + '<auditSubscribers>')
    f.write('    ' + '<MSISDN>' + row[0] + '</MSISDN>')
    f.write('    ' + '<OperationType>' + row[1] + '</OperationType>')
    f.write('    ' + '<ServiceIndication>' + row[2] + '</ServiceIndication>')
    f.write('    ' + '</auditSubscribers>')

# xml end root element

f.write('</Audit>')
f.close()
print("finished writing xml")