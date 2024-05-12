my_dict = {'a': 1, 'b': 2, 'c': 3}

keys = my_dict.keys()
values = my_dict.values()

print(keys)
print(values)

for i in keys:
    print(i)

for i in values:
    print(i)
    
my_dict['d'] = 4
my_dict['c'] = 6
print(my_dict)

del my_dict['c']
print(my_dict)

my_dict.pop('b')
print(my_dict)

for key in my_dict:
    print(key,':', my_dict[key])
    
for key,value in my_dict.items():
    print(key,'::',value)

square = {x : x ** 2 for x in range(1,5) }
print(square)


my_dict1 = {'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}}
print(my_dict1['a']['y'])

# dictionary main methods

print(my_dict.keys())   # Returns dict_keys(['a', 'b', 'c'])
print(my_dict.values()) # Returns dict_values([1, 2, 3])
print(my_dict.items())  # Returns dict_items([('a', 1), ('b', 2), ('c', 3)])

sorted_keys = sorted(my_dict.keys())
sorted_values = sorted(my_dict.values())
sorted_items = sorted(my_dict.items())

print(sorted_keys)
print(sorted_values)
print(sorted_items)

# merge dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = {**dict1,**dict2}
print(merged_dict)
