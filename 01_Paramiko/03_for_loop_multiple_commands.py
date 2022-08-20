import time

from paramiko import client
from getpass import getpass

hostname = 'nxos1.test.lab'
username = input("Enter Username:")

if not username:
    username = 'admin'
    print(f"No username provided, considering default username {username}")

password = getpass(f"Enter Password of the user {username}: ") or "admin"

commands = ['config t', 'int lo1001', 'ip address 1.1.1.1 255.255.255.0', 'end']

ssh_client = client.SSHClient()
ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())

ssh_client.connect(hostname=hostname, port=22, username=username, password=password, look_for_keys=False,
                   allow_agent=False)

print("Connected successfully")
device_access = ssh_client.invoke_shell()
device_access.send("terminal len 0\n")

for cmd in commands:
    device_access.send(f"{cmd}\n")
    time.sleep(1)
    output = device_access.recv(65535)
    print(output.decode(), end='')

device_access.send("show run int lo1001\n")
time.sleep(2)
output = device_access.recv(65535)
print(output.decode())

ssh_client.close()
