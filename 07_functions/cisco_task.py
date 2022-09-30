import sys
import time
import socket

from paramiko import client, ssh_exception

def cisco_cmd_executor(hostname, commands, username, password):
    try:
        print(f"\n{'#'*10}Connecting to the Device {hostname} {'#'*10}")
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, username=username, password=password,
                           port=22,
                           look_for_keys=False, allow_agent=False)
        print("Connected successfully")
        device_access = ssh_client.invoke_shell()
        device_access.send("term len 0\n")
        device_access.send("config t\n")
        for cmd in commands:
            device_access.send(f"{cmd}\n")
            time.sleep(1)
            output = device_access.recv(65000)
            print(output.decode(),end='')
        device_access.close()
        print(f"\n{'#' * 10}  Disconnected from the Device {hostname} {'#' * 10}")
    except socket.gaierror:
        print("Check the hostname")
    except ssh_exception.NoValidConnectionsError:
        print("SSH Port not reachable")
    except ssh_exception.AuthenticationException:
        print("Authentication failed, check the credentials")
    except:
        print("Exception occurred")
        print(sys.exc_info())
        # traceback.print_exception(*sys.exc_info())

vIOS1 = {'hostname': '192.168.0.61',
         'commands': ['int lo1001', 'no shut'],
         'username': 'admin',
         'password': 'admin'}

vIOS2 = {'hostname': '192.168.0.62',
         'commands': ['int lo1001', 'no shut'],
         'username': 'admin',
         'password': 'admin'}

vIOS3 = {'hostname': '192.168.0.91',
         'commands': ['int lo1001', 'no shut'],
         'username': 'admin',
         'password': 'admin'}


cisco_cmd_executor(**vIOS1)
cisco_cmd_executor(**vIOS2)

# cisco_cmd_executor('192.168.0.63', ['int lo1001', 'no shut'], 'admin', 'admin')