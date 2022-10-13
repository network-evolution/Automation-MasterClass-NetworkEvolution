"""
extensible markup language
###################
xmltodict:
      Unparse
Python  >>>    XML
Python  <<<    XML
       Parse
###################
"""
import xmltodict
from pprint import pprint
from lab_inventory import *

## Python to XML
# with open('py_to_xml.xml', 'w') as xml_out:
#     xml_out.write(xmltodict.unparse(xml_inventory_new, pretty= True))

## XML to Python
# with open('py_to_xml.xml') as xml_in:
#     new_inventory = xmltodict.parse(xml_in.read(), dict_constructor=dict)
# pprint(new_inventory)

# with open('all_int.xml') as xml_in:
#     int_details = xmltodict.parse(xml_in.read(), dict_constructor=dict)
# # pprint(int_details)
#
# interface = int_details['rpc-reply']['data']['native']['interface']
# pprint(interface)
#
# print(interface['GigabitEthernet'][0])
# print(interface['GigabitEthernet'][1])

import xml.etree.ElementTree as ET
tree = ET.parse('all_int.xml')
root = tree.getroot()
# print(root[0][0][0][1][0].text)
# print(root[0][0][0][1][1][0][0][0].text)

n = int(input("Enter Interface Number:"))
n = n - 1
int_number = root[0][0][0][n][0].text
int_ip = root[0][0][0][n][1][0][0][0].text


print(f"GigabitEthernet {int_number} - IP Address: {int_ip}")










