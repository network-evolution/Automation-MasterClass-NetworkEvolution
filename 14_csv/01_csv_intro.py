import csv
import time
import paramiko

print(csv.list_dialects())

d = csv.get_dialect('excel-tab')
print(dir(d))
print(d.delimiter.encode())
print(d.quotechar)

conf_dict = {'192.168.0.61': ['terminal len 0',
                              'config t',
                              'int gi0/0',
                              'no shut',
                              'exit',
                              'exit',
                              'show ip int brie',
                              'show run int gi0/0'],
             '192.168.0.62': ['terminal len 0',
                              'config t',
                              'int lo0',
                              'ip add 10.0.0.1 255.255.255.0',
                              'int lo1',
                              'ip add 11.0.0.1 255.255.255.0',
                              'do show run int loopback0',
                              'do show run int loopback1'],
             '192.168.0.91': ['terminal len 0', 'config t', 'int gi0/3', 'no shut'],
             'csr1.test.lab': ['terminal len 0',
                               'config t',
                               'int gi2',
                               'no shut',
                               'ip address 2.2.2.2 255.255.255.0',
                               'exit',
                               'exit',
                               'show ip int brie',
                               'show run int gi2']}


# for ip, conf_cmd in conf_dict.items():
#     print(f"Connecting to the device: {ip}")
#     for cmd in conf_cmd:
#         time.sleep(.5)
#         print(cmd)

session = paramiko.client.SSHClient()
session.load_system_host_keys()
session.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
for ip, conf_cmd in conf_dict.items():
    try:
        print(f"\n{'#' * 50}\nConnecting to the Device {ip}\n{'#' * 50} ")
        session.connect(hostname=ip,
                        username='admin',
                        password='admin',
                        look_for_keys=False,
                        allow_agent=False
                        )
        device_access = session.invoke_shell()
        print(f"\nExecuting Commands are\n{'~' * 22}\n{conf_dict[ip]}")
        for conf in conf_cmd:
            device_access.send(conf + '\n')
            time.sleep(1)
            output = device_access.recv(65000)
            print(output.decode('ascii'), end='')
            time.sleep(.5)
        session.close()
    except:
        print('Can not connect to the device')

print(f"\n{'#' * 50}\nCOMMAND EXECUTION COMPLETED\n{'#' * 50}\n")