
# from nornir import InitNornir
# from nornir_utils.plugins.functions import print_result, print_title
# from nornir_netmiko import netmiko_send_config, netmiko_send_command, netmiko_save_config
#
# print_title("NORNIR NETMIKO Multiple Tasks")
#
# nr = InitNornir(config_file="config.yaml")
# ios = nr.filter(platform='ios')
#
# def route_add(route_task):
#     route_task.run(task=netmiko_send_config, config_file='add_routes.txt')
#     route_task.run(task=netmiko_send_command, command_string='show run | i ip route')
#     route_task.run(task=netmiko_save_config)
#
# results = ios.run(task=route_add)
# print_result(results)

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_napalm.plugins.tasks import napalm_cli, napalm_configure

nr = InitNornir(config_file="config.yaml")

ios = nr.filter(platform='ios')

print_title("NAPALM Configure")

def add_route(route_task):
    route_task.run(task=napalm_configure, filename="remove_routes.txt")
    route_task.run(task=napalm_cli, commands=["show run | i ip route"])

results = ios.run(task=add_route)
print_result(results)

