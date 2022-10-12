from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_napalm.plugins.tasks import napalm_get

print_title("NAPALM GET TASK")
nr = InitNornir(config_file="config.yaml")

ios = nr.filter(platform='ios')
results = ios.run(task=napalm_get, getters=["facts", "interfaces_ip"])
print_result(results)