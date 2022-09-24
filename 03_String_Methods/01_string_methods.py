
username = 'admin1'
# print(dir(username))

# print(username.capitalize())
# print(username.casefold())
# print(username.center(20), "Hi")

# user_input = input("Enter Username:").casefold().strip().replace(" ","")
# if user_input == username:
#     print(f"Input {user_input} matched")
# else:
#     print("Not matched")
########################################################################

# ip = '192.168.0.1'
# device = 'router'
# print(f"IP Address is: {ip}\nDevice type is: {device}")

########################################################
'''find'''
# print(username.index('2'))

##############################################################
'''is decimal'''
# a_number = '\u0035'
# print(a_number)
# print(a_number.isdigit())
# print(a_number.isdecimal())

b_letter = 'A'
# print(b_letter.isascii())
##########################################################
'''is identifier  a-z, A-Z, 0-9, _ : should not start with number'''
# an_identifier = 'A123a_'
# print(an_identifier.isidentifier())
##########################################################
'''printable'''
printable = 'Hey there'
# print(printable.isprintable())
##########################################################
'''join'''
list1 = ['Cisco', "IOS", "17.3"]
# print('-'.join(list1))
# print('.'.join(list1))
##########################################################
'''ljust'''
# print("abc".ljust(18), '12345')
# print("abcabcabc".ljust(18), '12345')
# print("abcabc".ljust(18), '12345')
# print("abcrtui".ljust(18), '12345')

##########################################################
'''maketrans'''
# message = "Hey there.."
# trans = message.maketrans('e.', 'E!')
# print(message.translate(trans))

##########################################################
'''partition'''
message = "ip route 192.168.0.0"
# print(message.partition(" route "))

##########################################################
'''replace'''
message = "Hello there"
print(message.replace("there", "world"))

##########################################################
'''split'''
users = 'user1, user2, user3'
user_list = users.split(', ')
# print(user_list)
# for user in user_list:
#     print(f"Username is: {user}")
##########################################################
'''splitlines'''
print("user1\nuser2\nuser3".splitlines())

##########################################################
'''translate'''
trans = {46: 33}
print("Hey there..".translate(trans))

##########################################################
'''zfill'''
print('abc'.zfill(5))








