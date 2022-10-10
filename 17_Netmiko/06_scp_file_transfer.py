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
#                          source_file='config.txt',
#                          dest_file='config.txt',
#                          file_system='bootflash:',
#                          direction='put',
#                          overwrite_file=True,
#                          progress4=progress_bar)

transfer = file_transfer(net_connect,
                         source_file='csr1000v-rpboot.17.03.03.SPA.pkg',
                         dest_file='csr1000v-rpboot.17.03.03.SPA.pkg',
                         file_system='bootflash:',
                         direction='get',
                         overwrite_file=True,
                         progress4=progress_bar)
print(transfer)
net_connect.disconnect()