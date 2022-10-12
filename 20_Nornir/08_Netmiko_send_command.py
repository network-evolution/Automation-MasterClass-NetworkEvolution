## Netmiko Send Command
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_netmiko import netmiko_send_command

nr = InitNornir(config_file="config.yaml")

ios = nr.filter(platform='ios')
print_title("Nornir Netmiko Send Command")
get_results = ios.run(task=netmiko_send_command, command_string="show version")
print_result(get_results)