from ncclient import manager, xml_

lab_173 = {'host': '192.168.0.63',
           'port': 830,
           'username': 'admin',
           'password': 'admin',
           'hostkey_verify': False,
           'device_params': {'name': 'csr'}}

rtr_mgr = manager.connect(**lab_173)
save = """<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>"""
output = rtr_mgr.dispatch(xml_.to_ele(save))
print(output)

rtr_mgr.close_session()