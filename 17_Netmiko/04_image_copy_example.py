from netmiko import Netmiko

csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.63',
    'username': 'admin',
    'password': 'admin'
}
copy_cmd = 'copy bootflash:csr1000v-mono-universalk9.17.03.03.SPA.pkg bootflash:new.pkg'
net_connect = Netmiko(**csr)
print("Connected successfully")

run_df = net_connect.send_command(copy_cmd, expect_string="Destination filename")
print(run_df)
run_ov = net_connect.send_command("\n", expect_string="Do you want to over write")
print(run_ov)
run_c = net_connect.send_command("\n", expect_string="#", read_timeout=50)
print(run_c)
net_connect.disconnect()


