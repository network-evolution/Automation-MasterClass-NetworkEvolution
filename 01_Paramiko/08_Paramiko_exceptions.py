import sys
import time
import traceback

from paramiko import client, ssh_exception
from getpass import getpass
import socket

username = 'admin'
password = 'admin'
csr_cmd = ['config t', 'int lo1001', 'ip address 1.1.1.1 255.255.255.0', 'end']

def cisco_cmd_executor(hostname, commands):
    try:
        print(f"Connecting to the device {hostname}..")
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, port=22, username=username, password=password, look_for_keys=False,
                           allow_agent=False)

        print(f"Connected to the device {hostname}")
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

cisco_cmd_executor('csr1.test.lab', csr_cmd)
cisco_cmd_executor('192.168.0.20', csr_cmd)
