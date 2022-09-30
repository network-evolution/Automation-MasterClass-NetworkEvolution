name = input("Enter text:")

if name == 'admin':
    print("Matched with admin")
elif name in ['admin', 'user', 'operator']:
    print("Matched with users list")
else:
    print("Not matched with any name")


