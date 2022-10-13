from ncclient import manager

lab_173 = {'host': '192.168.0.63',
           'port': 830,
           'username': 'admin',
           'password': 'admin',
           'hostkey_verify': False,
           'device_params': {'name': 'csr'}}

rtr_mgr = manager.connect(**lab_173)
user_config = '''
    <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" >
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <username>
          <name>netconf_user</name>
          <privilege>15</privilege>
          <secret>
            <secret>password123</secret>
          </secret>
        </username>
      </native>
    </config>
'''

output = rtr_mgr.edit_config(user_config, target='running')
print(output)

rtr_mgr.close_session()