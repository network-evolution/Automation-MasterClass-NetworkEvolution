from netmiko import ConnectHandler, file_transfer, progress_bar

csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.63',
    'username': 'admin',
    'password': 'admin'
}

net_connect = ConnectHandler(**csr)
print("Connected successfully")

# transfer = file_transfer(net_connect,
#                          source_file='running-config',
#                          dest_file='running-config',
#                          file_system='system:',
#                          direction='get',
#                          overwrite_file=True,
#                          progress4=progress_bar)

transfer = file_transfer(net_connect,
                         source_file='startup-config',
                         dest_file='startup-config',
                         file_system='nvram:',
                         direction='get',
                         overwrite_file=True,
                         progress4=progress_bar)
print(transfer)
net_connect.disconnect()