from ncclient import manager

lab_173 = {'host': '192.168.0.63',
           'port': 830,
           'username': 'admin',
           'password': 'admin',
           'hostkey_verify': False,
           'device_params': {'name': 'csr'}}

rtr_mgr = manager.connect(**lab_173)
interface_config = '''
    <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" >
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <GigabitEthernet>
            <name>2</name>
            <ip>
              <address>
                <primary>
                  <address>22.2.2.2</address>
                  <mask>255.255.255.0</mask>
                </primary>
              </address>
            </ip>
          </GigabitEthernet>
        </interface>
      </native>
    </config>
'''

output = rtr_mgr.edit_config(interface_config, target='running')
print(output)

rtr_mgr.close_session()