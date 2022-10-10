import jinja2

## jinja2 Templates

# route1 = {'dest_sub': '11.1.1.1', 'dest_gw': '1.1.1.1'}
# route2 = {'dest_sub': '11.1.1.2', 'dest_gw': '1.1.1.2'}
# route3 = {'dest_sub': '11.1.1.3', 'dest_gw': '1.1.1.3'}
#
# # config = "ip route {{dest_sub}} 255.255.255.0 {{dest_gw}}"
# with open('static_route.j2') as file:
#     config = file.read()
# t1 = jinja2.Template(config)
# # print(type(t1))
#
# print(t1.render(route1))
# print(t1.render(route2))
# print(t1.render(route3))

#####################################################
'''for loop'''

# dest_subnet = ['21.0.0.0','22.0.0.0','23.0.0.0']
# route1 = {'dest_subs': dest_subnet, 'dest_gw': '1.1.1.1'}
#
# # config = '''
# # {%- for dest_sub in dest_subs %}
# # ip route {{dest_sub}} 255.255.255.0 {{dest_gw}}
# # {%- endfor %}
# # '''
# with open('static_route_with_for_loop.j2') as data:
#     config = data.read()
# t1 = jinja2.Template(config)
# print(t1.render(route1))

##########################################################
'''if'''

# dest_subnet = ['21.0.0.0','22.0.0.0','23.0.0.0']
# dest_subnet2 = ['21.0.0.2','22.0.0.2','23.0.0.2']
# #
# route1 = {'dest_subs': dest_subnet, 'dest_gw':'1.1.1.1', 'add_default': True}
# route2 = {'dest_subs': dest_subnet2, 'dest_gw':'1.1.1.1', 'add_default': True}
#
# with open('static_route_if.j2') as data:
#     config = data.read()
# t1 = jinja2.Template(config)
# print(t1.render(route2))

##############################################################
'''dictionary'''
#
# interface_dict = {
#     'interfaces':
#         {'Gi1': '1.1.1.1',
#          'Gi2': '2.2.2.2',
#          'Gi3': '3.3.3.3',
#          'Gi4': '3.3.3.4'
#          }
# }
#
# config = '''
# {%- for interface,ip in interfaces.items() %}
# interface {{interface}}
#   ip address {{ip}} 255.255.255.0
#   description ### {{interface}}  description ###
# {%- endfor %}'''
# t1 = jinja2.Template(config)
# print(t1.render(interface_dict))
###########################################################################
'''list of dicts'''
data = {'int_list': [{'name': 'Gi1', 'server': 'esxi1', 'vlan': '100'},
                     {'name': 'Gi2', 'server': 'esxi2', 'vlan': '101'},
                     {'name': 'Gi3', 'server': 'esxi2', 'vlan': '102'}
                     ]}

config = '''
{%- for interface in int_list %}
interface {{interface['name']}}
  description ### Connected to {{interface['server']}}
  switchport mode access
  switchport vlan {{interface['vlan']}}
{%- endfor %}'''

t1 = jinja2.Template(config)
print(t1.render(data))