import sys

# sys.path.append('/home/evolve/Documents/GitHub/Automation-MasterClass-NetworkEvolution/07_functions')
sys.path.insert(0, '/home/evolve/Documents/GitHub/Automation-MasterClass-NetworkEvolution/07_functions')
# print(sys.path)
from password_gen import user_cmd_gen

print(user_cmd_gen('admin1', 15))