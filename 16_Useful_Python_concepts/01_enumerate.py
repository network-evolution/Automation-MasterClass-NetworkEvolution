#### enumerate()

vendors = ['cisco', 'arista', 'juniper', 'cumulus', 'extreme']

# print(vendors.index('cumulus'))
# print(vendors[3])
#
# e = enumerate(vendors)
# print(e)

# for data in enumerate(vendors, start=10):
#     print(data)

# for index,name in enumerate(vendors):
#     print(index, name)

users = ['user1', 'user2', 'user3', 'user4']
search = input("Enter Username: ")
for index, name in enumerate(users):
    if name == search:
        print(f"User {search} index is {index}")
        break
else:
    print("Not found")

