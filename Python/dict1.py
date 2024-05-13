name = "ajaydev"

my_dict = {}
for i in name:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

print(my_dict)