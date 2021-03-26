import pandas as pd
import os
from xml.dom import minidom
import logging

logging.basicConfig(filename="xml_log.log", level=logging.DEBUG)
data_file = pd.read_csv("sample_input.csv", usecols=[0, 1, 2])

result = pd.read_csv('sample_input.csv')
mav_list = [list(i) for i in result.values]

list_subs = []

def uniqueSubscriber():
    for i in mav_list:
        flag = 1
        for j in list_subs:
            flag = 1
            if j[0] == i[0]:
                flag = 0
                break
        if flag:
            list_subs.append(i[:5])


uniqueSubscriber()

def singleAuditSub():
    root = minidom.Document()

    xml = root.createElement('Audit')
    xml.setAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    xml.setAttribute('xsi:noNamespaceSchemaLocation', 'schema.xsd')
    root.appendChild(xml)

    audit_subsciber = root.createElement('auditSubscribers')
    xml.appendChild(audit_subsciber)

    msidn = root.createElement('MSIDN')
    msidn.appendChild(root.createTextNode(str(list_subs[0][0])))
    audit_subsciber.appendChild(msidn)

    operation_type = root.createElement('OperationType')
    operation_type.appendChild(root.createTextNode(str(list_subs[0][1])))
    audit_subsciber.appendChild(operation_type)

    service_indication = root.createElement('ServiceIndication')
    service_indication.appendChild(root.createTextNode(str(list_subs[0][2])))
    audit_subsciber.appendChild(service_indication)

    xml_str = root.toprettyxml(indent="\t")

    save_path_file = "audit_subscriber.xml"

    with open(save_path_file, "w") as file:
        file.write(xml_str)
    logging.debug("Single Record Generated")


singleAuditSub()

def multipleAuditSubs():
    root = minidom.Document()

    xml = root.createElement('Audit')
    xml.setAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    xml.setAttribute('xsi:noNamespaceSchemaLocation', 'schema.xsd')
    root.appendChild(xml)

    for i in list_subs:
        audit_subsciber = root.createElement('auditSubscribers')
        xml.appendChild(audit_subsciber)
        msidn = root.createElement('MSIDN')
        msidn.appendChild(root.createTextNode(str(i[0])))
        audit_subsciber.appendChild(msidn)

        operation_type = root.createElement('OperationType')
        operation_type.appendChild(root.createTextNode(str(i[1])))
        audit_subsciber.appendChild(operation_type)

        service_indication = root.createElement('ServiceIndication')
        service_indication.appendChild(root.createTextNode(str(i[2])))
        audit_subsciber.appendChild(service_indication)

    xml_str = root.toprettyxml(indent="\t")

    save_path_file = "audit_subscribers.xml"

    with open(save_path_file, "w") as file:
        file.write(xml_str)
    logging.debug("Multiple Record Generated")


multipleAuditSubs()