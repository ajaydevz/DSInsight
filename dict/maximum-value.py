my_dict = {'a':100,'b':3094,'c':5444,'d':94532}
max_value = 0

for key,value in my_dict.items():
    if value > max_value:
        max_value = value
        max_key = key
           
print(max_key)
del my_dict[max_key]
print(my_dict)  