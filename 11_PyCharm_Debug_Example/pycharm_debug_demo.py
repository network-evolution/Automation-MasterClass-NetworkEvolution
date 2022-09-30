from password_gen import password_generator

users = ['user1', 'user2', 'user3']

##################################################
####         Dictionaries are Mutable     ########
##################################################
# final_user_list = []
# for user in users:
#     user_dict = {'username': user, 'password': password_generator()}
#     print(f"ID of user_dict inside loop is: {id(user_dict)}")
#     print(user_dict)
#     final_user_list.append(user_dict)
# print(final_user_list)
##################################################
####         Lists are Mutable            ########
##################################################
final_users_list = []

# print(f"ID of user_list out of loop is: {id(user_list)}")
for user in users:
    user_list = [user, password_generator()]
    print(f"ID of user_list inside loop is: {id(user_list)}")
    final_users_list.append(user_list)
print(final_users_list)