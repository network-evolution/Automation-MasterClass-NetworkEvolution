device_info_list = [
    ['name', 'router'],
    ['vendor', 'cisco'],
    ['model', 'vIOS'],
    ['ip', '1.1.1.1']
]
device_info = [
    ('name', 'router'),
    ('vendor', 'cisco'),
    ('model', 'vIOS'),
    ('ip', '1.1.1.1')
]
# device_dict = dict()
# for device in device_info:
#     device_dict[device[0]] = device[1]
# print(device_dict)
#
# device_dict_new = {device[0]: device[1] for device in device_info_list}
# print(device_dict_new)
#
# for key, value in device_dict_new.items():
#     print(key, value)

device_str = 'name:router, vendor:cisco, model:vIOS, ip: 1.1.1.1'

device_list = device_str.split(',')
# print(device_list)
device_dict = dict()
for item in device_list:
    k = item.split(':')
    # print(k)
    device_dict[k[0].strip()] = k[1].strip()

print(device_dict)


device_dict = {item.split(":")[0].strip():item.split(":")[1].strip() for item in device_str.split(',')}
print(device_dict)








