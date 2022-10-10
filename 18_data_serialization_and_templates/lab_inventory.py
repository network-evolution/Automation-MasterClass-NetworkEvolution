inventory_list = [
    {
        'ip': '192.168.0.1',
        'name': 'router1',
        'username': 'admin1',
        'password': 'admin1',
        'vendor': 'cisco',
        'os': 'ios'},
    {
        'ip': '192.168.0.2',
        'name': 'arista2',
        'username': 'admin2',
        'password': 'admin2',
        'vendor': 'arista',
        'os': 'eos'},
    {
        'ip': '192.168.0.3',
        'name': 'srx3',
        'username': 'admin3',
        'password': 'admin3',
        'vendor': 'juniper',
        'os': 'junos',
        'netconf': True,
        'license': None}
]
inventory_dict = {'192.168.0.1': {'name': 'router1',
                                  'username': 'admin1',
                                  'password': 'admin1',
                                  'vendor': 'cisco',
                                  'os': 'ios'},
                  '192.168.0.2': {'name': 'arista2',
                                  'username': 'admin2',
                                  'password': 'admin2',
                                  'vendor': 'arista',
                                  'os': 'eos'},
                  '192.168.0.3': {'name': 'srx3',
                                  'username': 'admin3',
                                  'password': 'admin3',
                                  'vendor': 'juniper',
                                  'os': 'junos',
                                  'netconf': True,
                                  'license': None}
                  }

inventory_list_of_dict = [{'192.168.0.1': {'name': 'router1',
                                           'username': 'admin1',
                                           'password': 'admin1',
                                           'vendor': 'cisco',
                                           'os': 'ios'}},
                          {'192.168.0.2': {'name': 'arista2',
                                           'username': 'admin2',
                                           'password': 'admin2',
                                           'vendor': 'arista',
                                           'os': 'eos'}},
                          {'192.168.0.3': {'name': 'srx3',
                                           'username': 'admin3',
                                           'password': 'admin3',
                                           'vendor': 'juniper',
                                           'os': 'junos'}}
                          ]

xml_inventory_new = {"inventory":
                         {"device": [{'name': 'router1',
                                      'username': 'admin1',
                                      'password': 'admin1',
                                      'vendor': 'cisco',
                                      'os': 'ios'},
                                     {'name': 'arista2',
                                      'username': 'admin2',
                                      'password': 'admin2',
                                      'vendor': 'arista',
                                      'os': 'eos'},
                                     {'name': 'srx3',
                                      'username': 'admin3',
                                      'password': 'admin3',
                                      'vendor': 'juniper',
                                      'os': 'junos'}
                                     ]}}
