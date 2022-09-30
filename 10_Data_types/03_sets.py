
lst1 = ['a', 'admin', 'ip', 'admin', 'pwd', 'pwd']
s1 = set(lst1)
# print(s1)
# print(dir(s1))

s1.add('new_data')
# print(s1)

# s1.update([6,7,8])
# s1.update((6,7,8))
# print(s1)

# s2 = {'r1','r2','r3','r4', 'r5'}
# s2.discard('r5')
# print(s2)

'''intersection'''
set1 = {'a','b','c'}
set2 = {'w','x','y','c','a'}
set3 = {'a'}
#
# print(set1.intersection(set2, set3))
#
# print(set1.difference(set2))
# print(set2.difference(set1))

'''symmetric difference'''
# print(set2.symmetric_difference(set1))

inventory = ['r1','r7','r5','r8','r4']
dc1 = ['r1','r2','r3']
dc2 = ['r5','r6','r7']

not_assigned_to_dcs = set(inventory).difference(dc1,dc2)
print(f"Not assigned to Any DC's: {not_assigned_to_dcs}")

missing_from_inv = (set(dc1).union(dc2)).difference(inventory)
print(f"Missing from Inventory: {missing_from_inv}")















