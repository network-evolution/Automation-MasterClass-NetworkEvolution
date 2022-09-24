from myconflib import cisco_cmd_executor, users_cmd_gen, user_cmd_gen

user_cmd = user_cmd_gen('test_admin1', 15)
# print(user_cmd)

# users_details = [{'name': 'user1', 'priv': 15},
#                  {'name': 'user2', 'priv': 15},
#                  {'name': 'user3', 'priv': 1}]

# users_cmd = users_cmd_gen(*users_details)
# print(users_cmd)

lab_csr1 = {'hostname': '192.168.0.63',
            'commands': user_cmd,
            'username': 'admin',
            'password': 'admin'}
# cisco_cmd_executor(hostname='192.168.0.63',
#                    commands=users_cmd,
#                    username='admin',
#                    password='admin')

cisco_cmd_executor(**lab_csr1)

