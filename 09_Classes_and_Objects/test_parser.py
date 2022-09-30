from cisco_parser import CiscoDevice

r1 = CiscoDevice(ip='192.168.0.63', username='admin', password='admin')
r2 = CiscoDevice('192.168.0.2', 'admin', 'admin')
# print(dir(r1))
# print(r1.port)
r1.connect()
print(r1.version())
print(r1.hostname())
r1.disconnect()
