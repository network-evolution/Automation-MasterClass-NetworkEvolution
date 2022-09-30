import sys
import time
import socket
from paramiko import client, ssh_exception
from datetime import datetime
import threading

start_time = datetime.now()


def cisco_cmd_executor(hostname, commands, username, password):
    try:
        print(f"\n{'#' * 10}Connecting to the Device {hostname} {'#' * 10}")
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, username=username, password=password,
                           port=22,
                           look_for_keys=False, allow_agent=False)
        print(f"Connected successfully to the device {hostname}")
        device_access = ssh_client.invoke_shell()
        device_access.send("term len 0\n")
        device_access.send("config t\n")
        print(f"Executing command in the device: {hostname}")
        with open(f"{hostname}.txt", 'a') as f:
            for cmd in commands:
                device_access.send(f"{cmd}\n")
                time.sleep(1)
                output = device_access.recv(65000)
                # print(output.decode(), end='')
                f.write(output.decode())

            device_access.close()
        print(f"\n{'#' * 10}Disconnected from the Device {hostname} {'#' * 10}")
    except socket.gaierror:
        print(f"Unable to connect to {hostname}: Check the hostname")
    except ssh_exception.NoValidConnectionsError:
        print(f"Unable to connect to {hostname}: SSH Port not reachable")
    except ssh_exception.AuthenticationException:
        print(f"Unable to connect to {hostname}: Authentication failed, check the credentials")
    except:
        print(f"Unable to connect to {hostname}: Exception occurred")
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

csr = {'hostname': '192.168.0.63',
       'commands': ['int lo1001', 'no shut'],
       'username': 'admin',
       'password': 'admin'}

hosts = [vIOS1, vIOS2, vIOS3, csr]

cisco_config_threads = []
for host in hosts:
    config_thread = threading.Thread(target=cisco_cmd_executor, kwargs=host)
    config_thread.start()
    cisco_config_threads.append(config_thread)
for thread in cisco_config_threads:
    thread.join()

##############################################
end_time = datetime.now()
print(end_time - start_time)
