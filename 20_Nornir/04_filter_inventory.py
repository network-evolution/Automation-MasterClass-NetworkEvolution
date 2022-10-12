from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

nr = InitNornir(config_file="config.yaml")

# print(nr.filter(site='IND').inventory.hosts.keys())
site_ind = nr.filter(site='IND')
# print(type(site_ind))
# print(dir(site_ind))
dc_blr = nr.filter(dc='BLR')

rtr1 = nr.filter(name='rtr1')
ios = nr.filter(platform='ios')

# results = nr.run(task=napalm_get, getters=["facts", "interfaces_ip"])
# results = site_ind.run(task=napalm_get, getters=["facts", "interfaces_ip"])
# results = dc_blr.run(task=napalm_get, getters=["facts", "interfaces_ip"])
# results = rtr1.run(task=napalm_get, getters=["facts", "interfaces_ip"])
results = ios.run(task=napalm_get, getters=["facts", "interfaces_ip"])
print_result(results)
