from netmiko import ConnectHandler, exceptions
csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.63',
    'username': 'admin123',
    'password': 'admin'
}
vIOS1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.60',
    'username': 'admin',
    'password': 'admin'
}
vIOS2 = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.62',
    'username': 'admin',
    'password': 'admin'
}
device_list = [csr, vIOS1, vIOS2]
for device in device_list:
    try:
        print(f"\n{'#' * 35}\nConnecting to the Device {device['host']}")
        net_connect = ConnectHandler(**device)
        print(f"Connected successfully to the Device {device['host']} ")
        print(net_connect.find_prompt())
        print(net_connect.send_command("show ip int brie"))
        net_connect.disconnect()
    except exceptions.NetmikoAuthenticationException:
        print(f"Authentication Failed on {device['host']}")
    except exceptions.NetmikoTimeoutException:
        print(f"Session timeout on {device['host']}")









