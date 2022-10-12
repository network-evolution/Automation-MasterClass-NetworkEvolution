from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli

nr = InitNornir(config_file="config.yaml")

ios = nr.filter(platform='ios')
print_title("NAPALM GET TASK")
get_results = ios.run(task=napalm_get, getters=["facts", "interfaces_ip"])
print_result(get_results)

print_title("NAPALM CLI TASK")
cli_results = ios.run(task=napalm_cli, commands=["show version", "show ip interface brief"])
# print_result(cli_results)
print(cli_results['rtr3'].result['show version'])