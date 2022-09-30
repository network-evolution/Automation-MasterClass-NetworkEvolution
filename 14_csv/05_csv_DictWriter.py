from csv import DictWriter

devices = [
    {'name': 'r1',
     'ip': '1.1.1.1',
     'vendor': 'cisco',
     'os': 'ios',
     'location': 'dc1'},
    {'ip': '2.2.2.2',
     'name': 'r2',
     'vendor': 'cisco',
     'os': 'ios'},
    {'name': 'r3',
     'ip': '3.3.3.3',
     'vendor': 'arista',
     'os': 'vEOS'}
]

list_of_keys = list(devices[0].keys())
print(list_of_keys)

with open('inventory.csv', 'w') as content:
    writer = DictWriter(content, fieldnames=list_of_keys)
    writer.writeheader()

    for data in devices:
        writer.writerow(data)

