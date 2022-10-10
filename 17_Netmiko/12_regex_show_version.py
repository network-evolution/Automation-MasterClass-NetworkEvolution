from netmiko import ConnectHandler, exceptions
import re

version_pattern = re.compile(r'Cisco .+ Software, Version (\S+)')
model_pattern = re.compile(r'cisco (\S+).+bytes of memory\.')
serial_no_pattern = re.compile(r'Processor board ID (\S+)')
uptime_pattern = re.compile(r'(.+) uptime is (.*)')
lab_csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.63',
    'username': 'admin',
    'password': 'admin'
}

try:
    net_connect = ConnectHandler(**lab_csr)
    print("Connected Successfully")
    output = net_connect.send_command('show version')
    # print(output)
    version_match = version_pattern.search(output)
    print('IOS Version'.ljust(18)+': ' + version_match.group(1))

    model_match = model_pattern.search(output)
    print('Model '.ljust(18)+': '+model_match.group(1))

    serial_no_match = serial_no_pattern.search(output)
    print('Serial Number '.ljust(18)+': '+serial_no_match.group(1))

    uptime_match = uptime_pattern.search(output)
    print('Host Name '.ljust(18)+': '+uptime_match.group(1))
    print('Device Uptime '.ljust(18)+': '+uptime_match.group(2))
    net_connect.disconnect()
except exceptions.NetmikoAuthenticationException:
    print(f"Authentication failed on {lab_csr['host']}")
except exceptions.NetmikoTimeoutException:
    print(f"Session timeout on {lab_csr['host']}")