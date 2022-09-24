import sys
import time
import traceback
from paramiko import client, ssh_exception
from getpass import getpass
import socket
import datetime
import re

version_pattern = re.compile(r'Cisco .+ Software, Version (\S+)')
model_pattern = re.compile(r'cisco (\S+).+bytes of memory\.')
serial_no_pattern = re.compile(r'Processor board ID (\S+)')
uptime_pattern = re.compile(r'(.+) uptime is (.*)')

new_cmd = ['show version']

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
        version_match = version_pattern.search(output)

        print('IOS Version'.ljust(18) + ': ' + version_match.group(1))

        model_match = model_pattern.search(output)
        print('Model '.ljust(18) + ': ' + model_match.group(1))

        serial_no_match = serial_no_pattern.search(output)
        print('Serial Number '.ljust(18) + ': ' + serial_no_match.group(1))

        uptime_match = uptime_pattern.search(output)
        print('Host Name '.ljust(18) + ': ' + uptime_match.group(1))
        print('Device Uptime '.ljust(18) + ': ' + uptime_match.group(2))

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

