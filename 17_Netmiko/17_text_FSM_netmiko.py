from netmiko import ConnectHandler, exceptions
from pprint import pprint
lab_csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.63',
    'username': 'admin',
    'password': 'admin'
}

try:
    print(f"\n{'#' * 35}\nConnecting to the lab_csr {lab_csr['host']}")
    net_connect = ConnectHandler(**lab_csr)
    print(f"Connected successfully to the lab_csr {lab_csr['host']} ")
    output = net_connect.send_command("show ip int brie", use_textfsm=True)

    print(f"Interface {output[0]['intf']} IP is {output[0]['ipaddr']}")
    print(f"Interface {output[1]['intf']} IP is {output[1]['ipaddr']}")
    net_connect.disconnect()
except exceptions.NetmikoAuthenticationException:
    print(f"Authentication Failed on {lab_csr['host']}")
except exceptions.NetmikoTimeoutException:
    print(f"Session timeout on {lab_csr['host']}")

