from lxml import etree
import logging
import os

os.chdir('C://Users//guptaran//Desktop//Python')

log_format = '%(asctime)s : %(message)s'
logging.basicConfig(filename="test.log", level=logging.DEBUG, format=log_format)
result = []
unique_result = []


def read_csv_file():
    logging.debug("Reading Record of Csv file successfully done")
    with open('sample_input.csv', 'r') as f:
        for line in f:
            words = line.split(',')
            result.append(words[0:3])

    print "\nPrinting Records of Csv .......\n"
    for i in result:
        print i


def unique_record_of_auditSubscriber():
    logging.debug("finding Unique Record of AuditSubscriber Successfully done")
    for row in result:
        MSISDN = row[0]
        flag = True
        for unique_row in unique_result:
            if MSISDN == unique_row[0]:
                flag = False
                break
        if flag:
            unique_result.append(row[:3])
    print "\nPrinting Unique Record Based on MSISDN of Csv .......\n"
    for i in unique_result:
        print i


def create_xml_for_single_auditSubscriber():
    logging.debug("Single Record Xml File Created for AuditSubscriber Successfully done")
    xsi = "http://www.w3.org/2001/XMLSchema-instance"
    schemaLocation = "schema.xsd"
    root_config = etree.Element("Audit",
                                attrib={"{" + xsi + "}noNamespaceSchemaLocation": schemaLocation},
                                nsmap={'noNamespaceSchemaLocation': schemaLocation, 'xsi': xsi
                                       })
    root_config = etree.SubElement(root_config, "Audit")
    auditSubscribers = etree.SubElement(root_config, "auditSubscribers")
    MSISDN = etree.SubElement(auditSubscribers, "MSISDN")
    MSISDN.text = str(result[0][0])
    OperationType = etree.SubElement(auditSubscribers, "OperationType")
    OperationType.text = str(result[0][1])
    ServiceIndication = etree.SubElement(auditSubscribers, "ServiceIndication")
    ServiceIndication.text = str(result[0][2])
    tree = etree.ElementTree(root_config)
    tree.write("singleAuditSubscriber.xml", encoding='utf-8', xml_declaration=True, pretty_print=True)


def create_xml_for_mutiple_auditSubscriber():
    logging.debug("Mutiple Record Xml File Created for AuditSubscriber- Successfully done")
    xsi = "http://www.w3.org/2001/XMLSchema-instance"
    schemaLocation = "schema.xsd"
    root_config = etree.Element("Audit",
                                attrib={"{" + xsi + "}noNamespaceSchemaLocation": schemaLocation},
                                nsmap={'noNamespaceSchemaLocation': schemaLocation, 'xsi': xsi
                                       })
    root_config = etree.SubElement(root_config, "Audit")
    for user in range(len(result)):
        auditSubscribers = etree.SubElement(root_config, "auditSubscribers")
        MSISDN = etree.SubElement(auditSubscribers, "MSISDN")
        MSISDN.text = str(result[user][0])
        OperationType = etree.SubElement(auditSubscribers, "OperationType")
        OperationType.text = str(result[user][1])
        ServiceIndication = etree.SubElement(auditSubscribers, "ServiceIndication")
        ServiceIndication.text = str(result[user][2])
        tree = etree.ElementTree(root_config)
        tree.write("multipleAuditSubscriber.xml", encoding='utf-8', xml_declaration=True, pretty_print=True)


def configuration_service_indication():
    logging.debug("configuration file filter on basis of user Service Indication Successfully done")
    input_string = raw_input("\nEnter a service (VM_SUBPROFILE / SMS_SUBPROFILE) to filter  \n")
    result1 = []
    for row1 in result:
        if input_string in row1:
            result1.append(row1)

    for i in result1:
        print i


if __name__ == "__main__":
    read_csv_file()
    unique_record_of_auditSubscriber()
    create_xml_for_single_auditSubscriber()
    create_xml_for_mutiple_auditSubscriber()
    configuration_service_indication()
