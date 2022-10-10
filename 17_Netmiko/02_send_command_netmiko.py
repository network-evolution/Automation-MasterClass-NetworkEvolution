from netmiko import Netmiko

csr = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.63',
    'username': 'admin',
    'password': 'admin'
}
net_connect = Netmiko(**csr)
print("Connected successfully")

# cmd_output = net_connect.send_command("show ip int brief")
cmd_output = net_connect.send_command("ping 1.2.3.4 repeat 5", read_timeout=20, expect_string=r"c.+#")
print(cmd_output)
net_connect.disconnect()