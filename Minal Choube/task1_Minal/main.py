import logging
from lxml import etree

import pandas as pd
from csv import reader

data_file = pd.read_csv("sample_csv.csv", usecols=[0, 1, 2])


def unique():
    list1 = []
    with open('sample_csv.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            if row[0] not in list1:
                print(row[0] + ' ' + row[1] + ' ' + row[2])
                list1.append(row[0])


def create_xml_for_single_auditSubscriber():
    logging.debug("Single Record Xml File Created ")
    xsi = "http://www.w3.org/2001/XMLSchema-instance"
    schemaLocation = "schema.xsd"
    config = etree.Element("Audit", attrib={"{" + xsi + "}noNamespaceSchemaLocation": schemaLocation},
                           nsmap={'noNamespaceSchemaLocation': schemaLocation, 'xsi': xsi})
    config = etree.SubElement(config, "Audit")
    auditSubscribers = etree.SubElement(config, "auditSubscribers")
    MSISDN = etree.SubElement(auditSubscribers, "MSISDN")
    MSISDN.text = str(data_file['MSISDN'][0])
    OperationType = etree.SubElement(auditSubscribers, "OperationType")
    OperationType.text = str(data_file['OperationType'][1])
    ServiceIndication = etree.SubElement(auditSubscribers, "ServiceIndication")
    ServiceIndication.text = str(data_file['ServiceIndication'][2])
    tree = etree.ElementTree(config)
    tree.write("singleAuditSubscriber.xml", encoding='utf-8', xml_declaration=True, pretty_print=True)


unique()
create_xml_for_single_auditSubscriber()
