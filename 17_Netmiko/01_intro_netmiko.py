from netmiko import Netmiko

## Netmiko
csr = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.63',
    'username': 'admin',
    'password': 'admin'
}

net_connect = Netmiko(**csr)
print("Connected successfully")
print(dir(net_connect))
# sh_output = net_connect.send_command("show run")
# print(sh_output)
print(net_connect.find_prompt())
print(net_connect.check_config_mode())
# print(net_connect.check_enable_mode())
net_connect.config_mode()
print(net_connect.check_config_mode())
print(net_connect.find_prompt())
net_connect.disconnect()
