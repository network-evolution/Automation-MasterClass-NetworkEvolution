my_list = ['1.1.1.1', '2.2.2.2', '4.4.4.4', '3.3.3.3', '11.1.1.1']
# print(my_list)
# print(my_list.count('1.1.1.1'))
# print(len(my_list))
# print(my_list[3])

# for data in my_list:
#     print(data)

my_list.append('7.7.7.7')
# print(my_list)


# print(my_list[2])
# print(my_list[-2])
# print(my_list[2:])
# print(my_list[2:4])
# print(my_list[:2])
# print(my_list[:-2])
# print(my_list[2:-2])
# print(my_list[-2:])

############################################################################

# l3 = ['a', 'b',[1,2,3,4],'d', {'ip':'1.1.1.1'}, 10]
# print(l3[2][2])
# print(l3[4]['ip'])
# print(l3[5])
# int_new = l3[5]
# print(int_new)
# print(type(int_new))

# my_list.remove('1.1.1.10')
# print(my_list)
# print(my_list.pop(1))
# print(my_list)

# print(list(range(0,20,2)))

# for i in range(len(my_list)):
#     print(f"{i+1} {my_list[i]}")


# while True:
#     v = ['', 'exit']
#     user_input = input("Enter the text:")
#     if user_input in v:
#         print("Exiting")
#         break
#     else:
#         print("Invalid Input")

# list2 = [2,3,4]
# my_list.extend(list2)
# print(my_list)


# my_list.reverse()
# print(my_list)



# users = ['Adfd', 'abdffrt', 'wwr', 'erdfghj']
#
# def length_calc(l):
#     return len(l)
#
# users.sort(key=length_calc)
# print(users)

list3 = [
    {'id': 1,
     'user': 'admin3',
     'password': 'pwd1'
     },
    {'id': 3,
     'user': 'admin1',
     'password': 'pwd1'
     },
    {'id': 2,
     'user': 'admin2',
     'password': 'pwd1'
     },
    {'id': 5,
     'user': 'admin1',
     'password': 'pwd1'
     }
]


def sort_logic(d):
    return d['user']

list3.sort(key=sort_logic, reverse=True)
print(list3)















