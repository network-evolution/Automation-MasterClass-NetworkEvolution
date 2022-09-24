import time
from paramiko import client, RSAKey
from getpass import getpass

linux_cmd = ['ls -larth', 'echo $USER', 'hostname', 'sdfgh']
pkey_pwd = getpass("Enter Pkey Password:")
key_file = RSAKey.from_private_key_file(filename='/home/evolve/.ssh/02_with_enc', password=pkey_pwd)
def exec_cmd_executor(hostname, commands, username):
    print(f"Connecting to the device {hostname}..")
    ssh_client = client.SSHClient()
    ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, port=22, username=username,
                       look_for_keys=True,
                       allow_agent=True,
                       pkey=key_file)

    print(f"Connected to the device {hostname}")

    for cmd in commands:
        print(f"\n{'#'*10} Executing {cmd}{'#'*10}")
        stdin, stdout, stderr = ssh_client.exec_command(cmd)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
            print(f"Error Occurred: {err}")


exec_cmd_executor('192.168.0.19', linux_cmd, 'evolve')
