from ncclient import manager
import xml.dom.minidom as md

lab_173 = {'host': '192.168.0.63',
           'port': 830,
           'username': 'admin',
           'password': 'admin',
           'hostkey_verify': False,
           'device_params': {'name': 'csr'}}

rtr_mgr = manager.connect(**lab_173)
output = rtr_mgr.get_config('running')
xmldata = md.parseString(str(output))
new_data = xmldata.toprettyxml(indent="  ")
print(new_data)
with open('new_conf.xml', 'w') as data:
    data.write(new_data)

rtr_mgr.close_session()