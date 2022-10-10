
import yaml
from pprint import pprint
from conf_data import conf_dict
from lab_inventory import *
d1 = {'rtr1': {'ip_addr': '10.1.1.1',
               'username': 'admin',
               'password': 'admin',
               'total_int': 5,
               'type': 'ios',
               'neighbors': ['10.10.10.1', '11.1.1.1']
               }}

# with open('file1.yaml') as yaml_data:
#     output = yaml.safe_load(yaml_data)
#
# pprint(output)
# print(output['rtr1'])
# print(output['rtr1']['ip_addr'])

# with open('conf_data.yaml', 'w') as yaml_data:
#     yaml_data.write(yaml.dump(conf_dict))

with open('inventory_list_of_dict.yaml', 'w') as yaml_data:
    yaml_data.write(yaml.dump(inventory_list_of_dict))