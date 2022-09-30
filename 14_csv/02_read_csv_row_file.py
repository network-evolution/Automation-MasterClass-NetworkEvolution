
from csv import reader
import paramiko
import time
from pprint import pprint
conf_dict = {}
with open('01_config_in_row.csv') as csv_data:
    csv_content = reader(csv_data)
    # print(dir(csv_content))
    for device in csv_content:
        # print(device)
        ip = device[0]
        if not ip:
            continue
        # print(ip)
        # print(device[1:])
        final_conf = []
        for conf in device[1:]:
            if not conf:
                continue
            final_conf.append(conf)
        conf_dict[ip] = final_conf

# pprint(conf_dict)
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

