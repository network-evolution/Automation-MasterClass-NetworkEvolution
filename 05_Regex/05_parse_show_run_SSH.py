import sys
import time
import traceback
from paramiko import client, ssh_exception
from getpass import getpass
import socket
import datetime
import re
from pprint import pprint

hostname_pattern = re.compile(r'hostname (\S+)')
domainname_pattern = re.compile(r'ip domain name (.+)')
pid_pattern = re.compile(r'license udi pid (\w+) sn (\S+)')
netconf_pattern = re.compile(r"netconf-yang\r\n")
username_pattern = re.compile(r'username (\S+) privilege (\d{1,2})')
interface_pattern = re.compile(r'interface (\S+)(\r\n.+?)+\r?\n?\s?ip address ([\d\.]+) ([\d\.]+)')
interface_prop_pattern = re.compile(r'interface (?P<name>\S+)(\r\n.+?)+\r?\n?\s?ip address (?P<ip_address>[\d\.]+) (?P<mask>[\d\.]+)')
default_route_pattern = re.compile(r'ip route 0.0.0.0 0.0.0.0.+?([\d.]+)\r\n')
static_route_pattern = re.compile(r'ip route (?P<dst_subnet>[^0][\d\.]+) (?P<mask>[^0][\d\.]+) (?P<next_hop>\S+)')

new_cmd = ['show running-config']

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
                time.sleep(5)
                output = device_access.recv(65535).decode()
                cmd_data.write(output)
                print(output)
        ssh_client.close()
        print("### Parsed output is ###")
        hostname_match = hostname_pattern.search(output)
        print('Hostname'.ljust(18) + ': ' + str(hostname_match.group(1)))

        domainname_match = domainname_pattern.search(output)
        print('Domain Name'.ljust(18) + ': ' + str(domainname_match.group(1)))

        pid_match = pid_pattern.search(output)
        print('PID'.ljust(18) + ': ' + str(pid_match.group(1)))
        print('SN'.ljust(18) + ': ' + str(pid_match.group(2)))

        netconf_match = netconf_pattern.search(output)
        if netconf_match:
            print('Netconf Enabled'.ljust(18) + ': Yes')
        else:
            print('Netconf Enabled'.ljust(18) + ': No')

        username_iter = username_pattern.finditer(output)
        user_list = []
        # print(username_iter)
        for user in username_iter:
            user_list.append(user.group(1))
        print('List of Users'.ljust(18) + ': ' + str(user_list))

        interface_iter = interface_pattern.finditer(output)
        interface_list = list()
        for interface in interface_iter:
            interface_list.append(interface.group(1))
            print(interface.group(0))
            print(interface.group(1))
        print('\nInterfaces with IP'.ljust(18) + ': ' + str(interface_list))

        interface_prop = interface_prop_pattern.finditer(output)
        interface_properties_list = list()
        for interface_conf in interface_prop:
            interface_properties_list.append(interface_conf.groupdict())
        pprint(interface_properties_list, indent=10)

        default_route_match = default_route_pattern.search(output)
        if default_route_match:

            print('\n' + 'Default Gateway'.ljust(18) + ': ' + default_route_match.group(1))
        else:
            print('\n' + 'Default Gateway'.ljust(18) + ': Not available')


        static_route_iter = static_route_pattern.finditer(output)
        static_route_list = list()
        for static_route in static_route_iter:
            static_route_list.append(static_route.groupdict())
        print('Static  Routes'.ljust(18) + ': ' + str(static_route_list))
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

