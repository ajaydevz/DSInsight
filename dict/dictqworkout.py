my_dict = {
    'apple':10,
    'banana':20,
    'orange':34
}

print(my_dict['apple'])

my_dict['grape'] = 65

print(my_dict)

my_dict['apple'] = 15

print(my_dict)

del my_dict['banana']

print(my_dict)

for k in my_dict:
    print(k)

for v in my_dict.values():
    print(v)

for k,v in my_dict.items():
    print(k,v)

my_dict = {'apple': 3, 'banana': 2, 'cherry': 5, 'date': 1}

sorted_dict = sorted(my_dict.items(), key=lambda item:item[1])
print(dict(sorted_dict))

key_sort = dict(sorted(my_dict.items()))
print(key_sort)


# Remove a key from a dictionary without using the del keyword.

my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
my_dict.pop('banana')
print(my_dict)
