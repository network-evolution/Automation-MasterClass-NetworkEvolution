inventory_dict = {'192.168.0.1': {'name': 'router1',
                                  'username': 'admin1',
                                  'password': 'admin1',
                                  'vendor': 'cisco',
                                  'os': 'ios'},
                  '192.168.0.2': {'name': 'arista2',
                                  'username': 'admin2',
                                  'password': 'admin2',
                                  'vendor': 'arista',
                                  'os': 'eos'},
                  '192.168.0.3': {'name': 'srx3',
                                  'username': 'admin3',
                                  'password': 'admin3',
                                  'vendor': 'juniper',
                                  'os': 'junos'},
                  '192.168.0.4': {'name': 'srx3',
                                  'username': 'admin3',
                                  'password': 'admin3',
                                  'vendor': 'juniper',
                                  'os': 'junos'}
                  }

# print(inventory_dict['192.168.0.2']['username'])

# k = list(inventory_dict.values())
# k = list(inventory_dict.keys())
# k = list(inventory_dict.items())
# print(k[0][1])
# print(len(inventory_dict))


# for device in inventory_dict.values():
#     print(device['name'])

# for ip, details in inventory_dict.items():
#     if details['vendor'] == 'juniper':
#         print(f"Juniper IP is {ip}")


dict1 = {'ip': '192.168.1.1',
         'hostname': 'router1',
         'vendor': 'cisco',
         'os': 'ios',
         'username': 'admin',
         'password': 'pwd123',
         'location': 'US'
         }

# dict1['ip_new'] = '1.1.1.1'
print(dir(dict1))
print(dict1.get('ip'))

dict1.setdefault("location", "IND")
print(dict1)

dict2 = {'ssh': True,
         'netconf': True,
         'restconf': False
         }

dict1.update(dict2)
print(dict1)


keys = ['r1', 'r2', 'r3', 'r4', 'r5']
value = 'router'
new_dict = dict.fromkeys(keys, value)
print(new_dict)