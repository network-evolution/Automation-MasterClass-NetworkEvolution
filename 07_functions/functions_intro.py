import string
import random


def user_cmd_gen(user, priv):
    password = ''.join(random.choices(string.ascii_uppercase +
                                      string.ascii_lowercase +
                                      string.digits, k=8))
    conf_list = [f"username {user} privilege {priv} secret {password}\n"]
    return conf_list
#####################################################################
# with open('test.txt', 'w') as file:
#     file.write(user_cmd_gen('admin1', 15))
#     file.write(user_cmd_gen('admin2', 15))
#     file.write(user_cmd_gen('admin3', 15))
#####################################################################
# print(user_cmd_gen('admin1', priv=15))

######################################################################
u_name = 'admin2'
u_priv = 15
# print(user_cmd_gen(u_name, u_priv))
######################################################
u_list = ['user2', 15]
# print(user_cmd_gen(*u_list))
# print(user_cmd_gen(*['user3', 15]))
# print(user_cmd_gen(*[u_list[0], u_list[1]]))
##########################################################

u_dict = {'user':'admin4', 'priv':15}
# print(user_cmd_gen(**u_dict))
##################################################

# def user_cmd_gen(user, priv, *args, **kwargs):
#     password = ''.join(random.choices(string.ascii_uppercase +
#                                       string.ascii_lowercase +
#                                       string.digits, k=8))
#
#     print(f"username {user} privilege {priv} secret {password}\n")
#     print("Commands are..")
#     for cmd in args:
#         print(cmd)
#     for data in kwargs:
#         print(f"{data} is: {kwargs[data]}")
# lst2 = ['conf t', 'int lo1001', 'no shut', 'sh ip int brie']
# dict2 = {'location': 'dc1', 'team':'SRE'}
# # user_cmd_gen('admin2', 15, *lst2, **dict2)
#
# for data in dict2.items():
#     print(data)
##################################################

user_dict = [{'name': 'user1', 'priv': 15},
             {'name': 'user2', 'priv': 15},
             {'name': 'user3', 'priv': 15}]

def users_cmd_gen(*args):
    cmd_list = []
    for user in args:
        password = ''.join(random.choices(string.ascii_uppercase +
                                          string.ascii_lowercase +
                                          string.digits, k=8))

        user_cmd = f"username {user['name']} privilege {user['priv']} secret {password}"
        cmd_list.append(user_cmd)
    return cmd_list

print(users_cmd_gen(*user_dict))
print(user_cmd_gen('admin5', 15))





