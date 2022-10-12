from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_napalm.plugins.tasks import napalm_cli, napalm_configure

nr = InitNornir(config_file="config.yaml")

ios = nr.filter(platform='ios')

print_title("NAPALM Configure")
conf_results = ios.run(task=napalm_configure, filename="remove_routes.txt")
print_result(conf_results)

print_title("NAPALM CLI TASK")
cli_results = ios.run(task=napalm_cli, commands=["show run | i ip route"])
print_result(cli_results)
