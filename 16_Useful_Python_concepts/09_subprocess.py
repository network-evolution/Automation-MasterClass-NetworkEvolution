import subprocess
## subprocess.run()

# subprocess.run('pwd')
# subprocess.run('ping 192.168.0.1 -c3', shell=True)
# subprocess.run(['ping' ,'192.168.0.1', '-c3'])

# s1 = subprocess.run('ping 192.168.0.1 -c3', capture_output=True, shell=True, text=True)
# print(s1)
# print(s1.stdout)

# s1 = subprocess.run('pwd1', capture_output=True, shell=True, text=True)
# print(s1.args)

# s1 = subprocess.run('pwd', capture_output=True, shell=True, text=True)
# if s1.stdout:
#     print(s1.stdout)
# else:
#     print(s1.stderr)

# s1 = subprocess.run('pwd1', capture_output=True, shell=True, text=True)
# if s1.returncode == 0:
#     print(s1.stdout)
# else:
#     print(s1.stderr)

with open('ping.txt', 'w') as ping_file:
    s1 = subprocess.run('ping 192.168.0.1', shell=True, text=True, stdout=ping_file)


