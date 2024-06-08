def return_dict():
    d = {'a':2,'b':4,'c':5}
    return d

print(return_dict())

result = return_dict()
print(result['a'])

# find middle element

my_dict = {'a':3,'b':4,'c':7}
keys = list(my_dict.keys())
print(keys)
middle_index = len(keys)//2
print(middle_index)
print(keys[middle_index])

print(my_dict[keys[middle_index]])