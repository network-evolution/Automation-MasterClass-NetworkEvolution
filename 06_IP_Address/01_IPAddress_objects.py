import ipaddress

# ip = ipaddress.IPv4Address('127.0.0.1')
# print(type(ip))
# print(ip.version)
# print(ip.max_prefixlen)
# print(ip.reverse_pointer)
# exp = ip.exploded
# print(type(exp))
# print(exp)
# print(ip.is_loopback)

try:
    ip_addr = ipaddress.ip_address(input("Enter IP:"))
except ValueError:
    print("Invalid IP")

