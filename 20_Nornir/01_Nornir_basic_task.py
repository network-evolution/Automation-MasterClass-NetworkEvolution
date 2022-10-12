## Nornir
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

nr = InitNornir(config_file="config.yaml")

results = nr.run(task=napalm_get, getters=["facts", "interfaces"])
print_result(results)
