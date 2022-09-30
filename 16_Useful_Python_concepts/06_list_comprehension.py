
# router_list = 'router1  ,  router2   , router3'

# new_list = router_list.split(',')
# print(new_list)
#
# final_list = []
# for new_device in new_list:
#     new_list = new_device.strip()
#     final_list.append(new_list)
# print(final_list)
#
# final_list = [new_device.strip() for new_device in router_list.split(',')]
# print(final_list)

router_list = 'router1  ,  router2   , router3, switch2, router4'

final_list = []
for new_device in router_list.split(','):
    if 'router' in new_device:
        final_list.append(new_device.strip())
print(final_list)

device = [new_device.strip() for new_device in router_list.split(',') if 'router' in new_device]
print(device)











