from operator import itemgetter
### itemgetter()
### sorted() - Function,  and sort() method

vendors = ['cisco', 'arista', 'juniper', 'cumulus', 'extreme', 'a', 'bb']
print(vendors)
# print(sorted(vendors, reverse=True))
vendors.sort()
print(vendors)

'''key based sorting'''

interface_list = [
    {'name': 'Gi1',
     'ip': '192.168.1.1',
     'mask': '255.255.255.0'},
    {'name': 'Gi2',
     'ip': '192.168.1.2',
     'mask': '255.255.255.0'},
    {'name': 'Gi3',
     'ip': '192.168.1.0',
     'mask': '255.255.255.0'},
    {'name': 'Gi4',
     'ip': '192.168.1.10',
     'mask': '255.255.255.0'},
]

dict_getter = itemgetter("name")
def sort_fn(e):
    return e["name"]
# print(sorted(interface_list, key=dict_getter))
# print(sorted(interface_list, key=sort_fn, reverse=True))


def get_len(e):
    return len(e)

print(sorted(vendors, key=get_len, reverse=True))















