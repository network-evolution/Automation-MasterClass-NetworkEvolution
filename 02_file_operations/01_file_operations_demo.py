import os

# print(os.getcwd())
# os.chdir('../01_Paramiko')
# print(os.getcwd())
# print(len(os.listdir()))
# print(f"Current working directory is {os.getcwd()}")
# print(os.system('ls -larth'))

files = (os.listdir())
files.sort()
for file in files:
    # print(file)
    with open(file) as file_data:
        if "paramiko" in file.casefold():
            print(print(f"\n\n{'#'*10} {file} {'#'*10}"))
            # print(type(file_data))
            # print(dir(file_data))
            print(file_data.read())

#########################################################################################

file1 = open('config1.txt', 'r')
print(dir(file1))
print(file1.read())
commands = file1.readlines()
for command in commands:
    print(command.rstrip('\n'))
file1.close()
###################################################################################
'''with open'''
with open('config1.txt') as file1:
    commands = file1.readlines()

for command in commands:
    print(command.rstrip('\n'))

###################################################################################

# with open('config2.txt', 'a') as file2:
#     file2.write("testdata3\ntestdata4\n")

############################################################################

# with open('test_file.pdf', 'rb') as source_file:
#     s = source_file.read()
#
# with open('new_file.pdf', 'wb') as dest_file:
#     dest_file.write(s)


os.remove('new_file.pdf')











