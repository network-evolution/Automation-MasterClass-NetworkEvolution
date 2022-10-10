from copy import deepcopy
my_list1 = [[1, 2, 3, 4], [4, 5, 6, 7]]
# my_list2 = my_list1

# print(id(my_list1))
# print(id(my_list2))

'''shallow copy'''

# my_list2 = my_list1.copy()
#
# print(f"ID of mylist1: {id(my_list1)}")
# print(f"ID of mylist2: {id(my_list2)}")
#
# print(f"mylist1: {my_list1}")
# print(f"mylist2: {my_list2}")
# my_list2[1][0] = 'new_msg'
#
# print(f"Current mylist1: {my_list1}")
# print(f"Updated mylist2: {my_list2}")
#####################
'''deepcopy'''

# my_list2 = deepcopy(my_list1)
#
# print(f"ID of mylist1: {id(my_list1)}")
# print(f"ID of mylist2: {id(my_list2)}")
#
# print(f"mylist1: {my_list1}")
# print(f"mylist2: {my_list2}")
# my_list1[0][0] = 'new_msg'
#
# print(f"Current mylist1: {my_list1}")
# print(f"Updated mylist2: {my_list2}")

'''dict'''

device_list1 = [
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
     'mask': '255.255.255.0',
     'speed': [10, 100, 1000],
     'user': [{'admin': {'priv': 15}},
              {'user1': {'priv': 15}}
              ]},
]
device_list2 = deepcopy(device_list1)
device_list2[3]["name"] = "Gi5"
print(f"Device list1: {device_list1}")
print(f"Device list2: {device_list2}")