from tabulate import tabulate
from operator import itemgetter
### tabulate ()


interface_list = [
    {'name': 'Gi1',
     'ip': '192.168.1.1',
     'mask': '255.255.255.0'},
    {'name': 'Gi2',
     'ip': '192.168.1.2',
     'mask': '255.255.255.0'},
    {'name': 'Gi3',
     'ip': '192.168.1.3',
     'mask': '255.255.255.0'},
    {'ip': '192.168.1.0',
        'name': 'Gi4',
     'mask': '255.255.255.0'},
]
# dict_getter = itemgetter("ip")
# interface_list.sort(key=dict_getter)
# print(tabulate(interface_list, tablefmt='fancy_grid'))

hdr = ['Name', 'IP', "Mask"]
value_list = []
for intf in interface_list:
    value_list.append(list(intf.values()))

# print(value_list)
print(tabulate(value_list, headers=hdr, tablefmt="fancy_grid"))












