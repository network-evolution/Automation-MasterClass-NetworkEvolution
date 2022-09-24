import ipaddress

ip_subnet = ipaddress.ip_network('192.168.0.0/24')
# print(type(ip_subnet))
# print(dir(ip_subnet))

# print(ip_subnet.network_address)
# print(ip_subnet.broadcast_address)
# print(ip_subnet.netmask)
# print(ip_subnet.num_addresses)
# print(ip_subnet.prefixlen)
# print(ip_subnet.exploded)
# print(ip_subnet.hostmask)
# print(ip_subnet.reverse_pointer)
# print(ip_subnet.with_prefixlen)
# print(ip_subnet.version)
# print(ip_subnet.max_prefixlen)

# print(ip_subnet.overlaps(ipaddress.ip_network('192.168.0.5/32')))

# for ip in ip_subnet.hosts():
#     print(ip)

# ip_add1 = ipaddress.ip_address('192.168.1.1')
# print(ip_add1 in ip_subnet)

new_exclude = ipaddress.ip_network('192.168.0.5')
l1 = ip_subnet.address_exclude(new_exclude)
for ip in l1:
    print(ip)