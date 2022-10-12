## Netmiko Send Config
# from nornir import InitNornir
# from nornir_utils.plugins.functions import print_result, print_title
# from nornir_netmiko import netmiko_send_config
#
# nr = InitNornir(config_file="config.yaml")
# ios = nr.filter(platform='ios')
#
# print_title("Nornir Netmiko Send Config")
# commands = ['no ip route 1.1.1.1 255.255.255.255 10.10.10.10',
#             'no ip route 1.1.1.2 255.255.255.255 10.10.10.10']
#
# get_results = ios.run(task=netmiko_send_config, config_commands=commands)
# print_result(get_results)


from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_netmiko import netmiko_send_config

nr = InitNornir(config_file="config.yaml")
ios = nr.filter(platform='ios')

print_title("Nornir Netmiko Send Config")


get_results = ios.run(task=netmiko_send_config, config_file='add_routes.txt')
print_result(get_results)