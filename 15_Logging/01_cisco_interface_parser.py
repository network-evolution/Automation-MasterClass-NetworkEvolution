import paramiko
import time
import re
import os
import sys
import socket
import schedule
###############
# Levels:
# CRITICAL 50
# ERROR    40
# WARNING  30
# INFO     20
# DEBUG    10
###############

# 01 import logging
import logging.handlers

EMAIL_ID = os.environ.get("EMAIL_ID")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

# 02 Define Logger
logger = logging.getLogger("interface_parser")

# 03 Set minimum logging level for logger
logger.setLevel(logging.DEBUG)

# 04 Create Handlers
file_handler_info = logging.FileHandler('show_ip_int_info.log')
file_handler_debug = logging.FileHandler('show_ip_int_debug.log')
stream_handler = logging.StreamHandler(sys.stdout)
smtp_handler = logging.handlers.SMTPHandler(mailhost=('smtp.gmail.com', 587),
                                            fromaddr=EMAIL_ID,
                                            toaddrs=['networkevolution.in@gmail.com'],
                                            subject="Log Alert",
                                            credentials=(EMAIL_ID, EMAIL_PASSWORD),
                                            secure=())

# 05 Create specific log level for Handlers
file_handler_info.setLevel(logging.INFO)
file_handler_debug.setLevel(logging.DEBUG)
stream_handler.setLevel(logging.WARNING)
smtp_handler.setLevel(logging.CRITICAL)

# 06 Create formatter
formatter = logging.Formatter('%(asctime)s - %(process)d-  %(name)s - %(levelname)s - %(message)s')
file_handler_info.setFormatter(formatter)
file_handler_debug.setFormatter(formatter)
stream_handler.setFormatter(formatter)
smtp_handler.setFormatter(formatter)
# 07 Add Handlers
logger.addHandler(file_handler_info)
logger.addHandler(file_handler_debug)
logger.addHandler(stream_handler)
logger.addHandler(smtp_handler)
lab_csr = {
    'host': '192.168.0.63',
    'username': 'admin',
    'password': 'admin'
}
devnet_csr = {
    'host': 'ios-xe-mgmt-latest.cisco.com',
    'username': 'developer',
    'password': 'C1sco12345'
}


int_pattern = re.compile(r'(\S+)\s+(([\d\.]+)|unassigned)\s+\S+\s+\S+\s+(up|administratively down)\s+(\S+)')


def cisco_interface_parser(host, username, password):
    try:
        print(f"\n{'#' * 55}\nConnecting to the Device {host}\n{'#' * 55} ")
        logger.info(f"Connecting to the Device {host}")
        session = paramiko.client.SSHClient()
        session.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        session.connect(host, port=22,
                        username=username,
                        password=password,
                        look_for_keys=False,
                        allow_agent=False)
        logger.info("Connected Successfully")
        device_access = session.invoke_shell()
        logger.info("Executing 'show ip interface brief'")
        device_access.send(b'term length 0\n')
        device_access.send(b'show ip interface brief\n')
        time.sleep(3)
        output = (device_access.recv(65000).decode())
        logger.info("Received Output")
        logger.debug(f"Output Data is: \n {output}")
        print(output)
        int_iter = int_pattern.finditer(output)
        int_list = list()
        for intf in int_iter:
            int_dict = dict()
            int_dict['int'], int_dict['ip'], int_dict['status'] = intf.group(1), intf.group(2), intf.group(4)
            if int_dict['int'] == 'Loopback1001' and int_dict['status'] == 'administratively down':
                logger.critical("Loopback 1001 is Down")
                print("Loopback 1001 is Down")
            print(int_dict)
            int_list.append(int_dict)
        logger.info("Storing parsed output")
        logger.debug(f"Parsed Output is:\n {int_list}")
        print(f"\n{'#' * 55}\nFinished Executing Script\n{'#' * 55} ")
        session.close()
    except paramiko.ssh_exception.AuthenticationException:
        # print("Authentication Failed")
        logger.critical("Authentication Failed")
    except socket.gaierror:
        print("Not resolvable: Check the name")
        logger.error("Not resolvable: Check the name")
    except:
        print(sys.exc_info())
        print("Can not connect to Device")
        logger.critical("Unable to connect")


# cisco_interface_parser(**lab_csr)
schedule.every(20).seconds.do(cisco_interface_parser, **lab_csr)

while True:
    schedule.run_pending()
    time.sleep(1)