import time
import paramiko
import re
class CiscoDevice:
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = 22

    def connect(self):
        print(f"Connecting to the device {self.ip}")
        session = paramiko.client.SSHClient()
        session.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        session.connect(hostname=self.ip,
                        username=self.username,
                        password=self.password,
                        look_for_keys=False, allow_agent=False)

        self.device_access = session.invoke_shell()
        self.device_access.send('terminal len 0\n')
        time.sleep(2)
        print("Connected to the device\n")

    def get_show_output(self, show_command):
        self.device_access.send(f"{show_command}\n")
        time.sleep(3)
        sh_output = self.device_access.recv(65000).decode()
        return sh_output

    def version(self):
        sh_ver_output = self.get_show_output('show version')
        version_pattern = re.compile(r'Cisco .+ Software, Version (\S+)')
        version_match = version_pattern.search(sh_ver_output)
        return 'IOS Version'.ljust(18) + ': ' + version_match.group(1)

    def hostname(self):
        sh_run_output = self.get_show_output('show run')
        hostname_pattern = re.compile(r'hostname (\S+)')
        host_match = hostname_pattern.search(sh_run_output)
        return 'Hostname'.ljust(18) + ': ' + str(host_match.group(1))

    def disconnect(self):
        self.device_access.close()
        print("\nClosed SSH Connection")




