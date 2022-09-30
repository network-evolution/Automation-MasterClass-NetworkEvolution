
t1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'a')
print(type(t1))
print(dir(t1))
print(t1.index('a'))

l1 = list(t1)
print(l1)
l1.append('new_data')
t2 = tuple(l1)
print(t2)