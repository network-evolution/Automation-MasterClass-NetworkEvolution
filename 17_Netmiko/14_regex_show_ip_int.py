from netmiko import ConnectHandler, exceptions
import re
from pprint import pprint
int_pattern = re.compile(r'(\S+)\s+(([\d\.]+)|unassigned)\s+\S+\s+\S+\s+(up|administratively down)\s+(\S+)')


lab_csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.63',
    'username': 'admin',
    'password': 'admin'
}
try:
    net_connect = ConnectHandler(**lab_csr)
    print("Connected Successfully")
    output = net_connect.send_command('show ip int brief')
    # print(output)
    int_iter = int_pattern.finditer(output)
    int_list = list()
    for intf in int_iter:
        int_dict = dict()
        int_dict['int_name'] = intf.group(1)
        int_dict['ip'] = intf.group(2)
        int_dict['status'] = intf.group(5)
        int_list.append(int_dict)
    pprint(int_list)
    net_connect.disconnect()
except exceptions.NetmikoAuthenticationException:
    print(f"Authentication failed on {lab_csr['host']}")
except exceptions.NetmikoTimeoutException:
    print(f"Session timeout on {lab_csr['host']}")