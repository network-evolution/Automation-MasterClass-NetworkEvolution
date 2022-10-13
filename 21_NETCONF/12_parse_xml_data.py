
import xml.etree.ElementTree as ET
from ncclient import manager

lab_173 = {'host': '192.168.0.63',
           'port': 830,
           'username': 'admin',
           'password': 'admin',
           'hostkey_verify': False,
           'device_params': {'name': 'csr'}}

rtr_mgr = manager.connect(**lab_173)
interface_filter = '''
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface/>
      </native>
    </filter>
'''

output = rtr_mgr.get_config('running', interface_filter)

root = ET.fromstring(str(output))

n = int(input("Enter Interface Number:"))
n = n - 1
int_number = root[0][0][0][n][0].text
int_ip = root[0][0][0][n][1][0][0][0].text


print(f"GigabitEthernet {int_number} - IP Address: {int_ip}")