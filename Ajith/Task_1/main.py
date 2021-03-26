import csv, logging, configparser, os
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString


INVALID_CONFIG_MSG = 'Invalid config file. See default.log for more details'

logging.basicConfig(filename='default.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s',
                    datefmt='%d-%m-%Y %I:%M:%S %p')

logging.info('script started and logging enabled')

logging.info('reading config file to get config settings and file names')
if not os.path.exists('sample.cfg'):
    logging.critical('config file does not exist or it is not named "sample.cfg"')
    raise ValueError('config file does not exist or it is not named "sample.cfg"')
config = configparser.ConfigParser()
config.read('sample.cfg')

csvfilename = config.get('filenames', 'infile', fallback=None)
if csvfilename is None:
    logging.critical('config file does not contain input file name')
    raise ValueError(INVALID_CONFIG_MSG)

data_dict = {}
with open(csvfilename, newline='') as csvfile:
    logging.info(f'started reading {csvfilename}')
    ipreader = csv.reader(csvfile)
    for row in ipreader:
        data_dict.setdefault(row[0], []).append((row[2], row[3]))
logging.info(f'closed {csvfilename}')
logging.debug(f'data_dict = {data_dict}')

service_indication = config.get('settings', 'service_indication', fallback=None)
if service_indication is None:
    logging.critical('config file does not contain service_indication setting')
    raise ValueError(INVALID_CONFIG_MSG)
logging.debug(f'service_indication = {service_indication}')

filtered_data = []
logging.info('started filtering data as per given config settings')
for msisdn, data in data_dict.items():
    for tup in data:
        if tup[1] == service_indication:
            filtered_data.append((msisdn, tup[0], tup[1]))
logging.info('filtering completed')
logging.debug(f'filtered_data = {filtered_data}')

batch_size = config.getint('settings', 'batch_size', fallback=None)
if batch_size is None:
    logging.critical('config file does not contain batch_size setting')
    raise ValueError(INVALID_CONFIG_MSG)
logging.debug(f'batch_size = {batch_size}')

count = 0
xml_root = ET.Element('Audit')
logging.info('started building xml')
for sub_tup in filtered_data:
    xml_child = ET.SubElement(xml_root, 'auditSubscribers')
    xml_msisdn = ET.SubElement(xml_child, 'MSISDN')
    xml_msisdn.text = sub_tup[0]
    xml_optype = ET.SubElement(xml_child, 'OperationType')
    xml_optype.text = sub_tup[1]
    xml_service = ET.SubElement(xml_child, 'ServiceIndication')
    xml_service.text = sub_tup[2]
    count += 1
    if count == batch_size:
        logging.debug(f'reached max({batch_size}) records while building xml')
        break

xml_root.set('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance')
xml_root.set('xsi:NoNamespaceSchemaLocation','schema.xsd')
xml_string = ET.tostring(xml_root, encoding='UTF-8', xml_declaration=True).decode()
xml_dom = parseString(xml_string)
xml_pretty_string = xml_dom.toprettyxml(indent='   ', encoding='UTF-8').decode()

logging.info('completed building xml')

xmlfilename = config.get('filenames', 'outfile', fallback=None)
if xmlfilename is None:
    logging.critical('config file does not contain output file name')
    raise ValueError(INVALID_CONFIG_MSG)

with open(xmlfilename, 'w') as outfile:
    logging.info(f'started writing xml to {xmlfilename}')
    outfile.write(xml_pretty_string)
logging.info(f'completed writing xml to {xmlfilename}')

logging.info('script execution completed. exiting')
