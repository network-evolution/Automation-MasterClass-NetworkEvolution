from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")

# print(nr.inventory)
# print(dir(nr.inventory))
# print(nr.inventory.hosts)
# print(nr.inventory.groups)
#
# print(nr.inventory.defaults.username)
# print(nr.inventory.defaults.password)
#
# all_hosts = nr.inventory.hosts
# for host in all_hosts:
#     print(host)

r1_host = nr.inventory.hosts['rtr1']
# print(type(r1_host))
# print(dir(r1_host))
# print(r1_host.platform)
# print(r1_host.data)
# print(r1_host['site'])
# print(r1_host.groups)

cisco_grp = nr.inventory.groups['cisco_group']
# print(cisco_grp.platform)

