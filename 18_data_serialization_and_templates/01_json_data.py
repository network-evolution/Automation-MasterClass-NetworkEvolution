"""
####################
Python      Json
--------------------
dict	    object
list,tuple	array
str	        string
int,float	number
True	    true
False	    false
None	    null
###################
      dump
Python >>> JSON
Python <<< JSON
      load
###################
"""
import json
from lab_inventory import *
## dump : directly saves to a file as json data
# with open('inventory_dict.json', 'w') as data:
#     json.dump(inventory_dict, data, indent=4)

## dumps : converts json to string
# with open('lab_data.json', 'w') as data:
#     st = json.dumps(inventory_list, indent=4)
#     data.write(st)
#
# print(st)
# print(type(st))

## load : reads directly from file: converts to python format
# with open('lab_data.json') as file:
#     output = json.load(file)
# print(output)


## loads: converts string to python format
with open('lab_data.json') as file:
    json_data = file.read()
print(json_data)

output = json.loads(json_data)
print(output)