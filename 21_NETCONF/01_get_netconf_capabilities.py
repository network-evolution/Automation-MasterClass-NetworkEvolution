# from ncclient import manager
#
# lab_173 = {'host': '192.168.0.63',
#            'port': 830,
#            'username': 'admin',
#            'password': 'admin',
#            'hostkey_verify': False,
#            'device_params': {'name': 'csr'}}
#
# rtr_mgr = manager.connect(**lab_173)
# for rtr_capabilities in rtr_mgr.server_capabilities:
#     print(rtr_capabilities)
# print(rtr_mgr.connected)
# rtr_mgr.close_session()
# print(rtr_mgr.connected)

##########################
"""get schema"""

from ncclient import manager

lab_173 = {'host': '192.168.0.63',
           'port': 830,
           'username': 'admin',
           'password': 'admin',
           'hostkey_verify': False,
           'device_params': {'name': 'csr'}}

rtr_mgr = manager.connect(**lab_173)
schema = rtr_mgr.get_schema("ietf-interfaces")
print(schema)
rtr_mgr.close_session()