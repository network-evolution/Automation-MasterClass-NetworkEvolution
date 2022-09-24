import ipaddress
from pprint import pprint
import sys
import time
from paramiko import client, ssh_exception
import socket
import datetime
import re

int_pattern = re.compile(r'(\S+)\s+(([\d\.]+)|unassigned)\s+\S+\s+\S+\s+(up|administratively down)\s+(\S+)')

new_cmd = ['show ip interface brief']
ip_subnet = ipaddress.IPv4Network(input("Enter Subnet to match:"))
def cisco_cmd_executor(hostname, commands, username, password):
    try:
        print(f"Connecting to the device {hostname}..")
        now = datetime.datetime.now().replace(microsecond=0)
        current_conf_file = f"{now}_{hostname}.txt"
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, port=22, username=username, password=password, look_for_keys=False,
                           allow_agent=False)

        print(f"Connected to the device {hostname}")
        device_access = ssh_client.invoke_shell()
        device_access.send("terminal len 0\n")
        with open(current_conf_file, 'w') as cmd_data:
            for cmd in commands:
                device_access.send(f"{cmd}\n")
                time.sleep(1)
                output = device_access.recv(65535).decode()
                cmd_data.write(output)
                print(output)
        ssh_client.close()
        print("### Parsed output is ###")
        int_iter = int_pattern.finditer(output)
        int_list = list()
        for intf in int_iter:
            int_dict = dict()
            int_dict['int_name'] = intf.group(1)
            int_dict['ip'] = intf.group(2)
            int_dict['status'] = intf.group(5)
            int_list.append(int_dict)
        pprint(int_list)
        print(f"### Interfaces part of subnet {ip_subnet} ###")
        for intf in int_list:
            try:
                ip = ipaddress.IPv4Address(intf['ip'])
                if ip in ip_subnet:
                    print(intf['int_name'], ip)
            except ValueError:
                continue
    except ssh_exception.NoValidConnectionsError:
        print("SSH Port not reachable")
    except socket.gaierror:
        print("Check the hostname")
    except ssh_exception.AuthenticationException:
        print("Authentication failed, check credentials")

    except:
        print("Exception Occurred")
        print(sys.exc_info())
        # traceback.print_exception(*sys.exc_info())

cisco_cmd_executor('csr1.test.lab', new_cmd, 'admin', 'admin')
cisco_cmd_executor('csr2.test.lab', new_cmd, 'admin', 'admin')


