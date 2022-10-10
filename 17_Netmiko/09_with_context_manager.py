from netmiko import ConnectHandler

csr = {
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
    'host': '192.168.0.61',
    'username': 'admin',
    'password': 'admin'
}

device_list = [csr, vIOS1, vIOS2]

for device in device_list:
    with ConnectHandler(**device) as net_connect:
        print("Connected successfully")
        show_cmd = net_connect.send_command("show ip interface brief")
        print(show_cmd)

    


