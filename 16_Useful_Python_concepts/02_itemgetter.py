from operator import itemgetter
### itemgetter()

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
    {'name': 'Gi4',
     'ip': '192.168.1.0',
     'mask': '255.255.255.0'},
]
#
# dict_getter = itemgetter('ip', 'name', 'mask')
# print(dict_getter)

# print(dict_getter(interface_list[0]))

# for interface in interface_list:
#     i = dict_getter(interface)
#     print(i[2])
# ip_list, int_list, mask_list = [], [], []
# for interface in interface_list:
#     i = dict_getter(interface)
#     ip_list.append(i[0])
#     int_list.append(i[1])
#     mask_list.append(i[2])
# print(ip_list, int_list, mask_list)

#####################################
vendors = ['cisco', 'arista', 'juniper', 'cumulus', 'extreme']
list_getter = itemgetter(2)
# print(list_getter(vendors))

for vendor in vendors:
    print(list_getter(vendor))


