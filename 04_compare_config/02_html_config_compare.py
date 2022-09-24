import difflib
import sys
import time
from paramiko import client, ssh_exception
import socket
import datetime
import webbrowser

with open('show_run.txt', 'r') as conf_file:
    new_cmd = conf_file.readlines()

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
                output = device_access.recv(65535)
                cmd_data.write(output.decode())
                print(output.decode(), end='')
        ssh_client.close()
        print("\nDisconnected from the device")
        with open('golden_conf.txt') as ref:
            ref_data = ref.readlines()
        with open(current_conf_file) as curr:
            curr_data = curr.readlines()
        conf_compare = difflib.HtmlDiff().make_file(fromlines=ref_data,
                                                    tolines=curr_data,
                                                    fromdesc="Golden Config",
                                                    todesc="Current Config")
        # print(conf_compare)
        with open('diff.html', 'w') as new_diff:
            new_diff.write(conf_compare)
        webbrowser.open_new_tab('diff.html')
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

