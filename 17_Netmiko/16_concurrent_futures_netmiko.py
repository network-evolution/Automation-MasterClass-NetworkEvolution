from netmiko import ConnectHandler, exceptions
from datetime import datetime
import concurrent.futures as cf

lab_csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.63',
    'username': 'admin',
    'password': 'admin'
}
vIOS1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.61',
    'username': 'admin',
    'password': 'admin'
}
vIOS2 = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.62',
    'username': 'admin',
    'password': 'admin'
}
hosts = [lab_csr, vIOS1, vIOS2]
start_time = datetime.now()

def netmiko_connect(**device):
    try:
        net_connect = ConnectHandler(**device)
        print(f"Connected Successfully to the Device: {device['host']}")
        output = net_connect.send_command('show ip int brief')
        # print(output)
        print(f"Writing output to the File: {device['host']}.txt")
        with open(f"{device['host']}.txt", 'w') as data:
            data.write(output)
        net_connect.disconnect()
    except exceptions.NetmikoAuthenticationException:
        print(f"Authentication failed on {device['host']}")
    except exceptions.NetmikoTimeoutException:
        print(f"Session timeout on {device['host']}")

with cf.ThreadPoolExecutor() as executor:
    total_output = [executor.submit(netmiko_connect, **host) for host in hosts]

end_time = datetime.now()
print(end_time - start_time)