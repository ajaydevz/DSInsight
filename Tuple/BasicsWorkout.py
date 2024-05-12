# single element

my_tuple = (40,)
print(my_tuple)
print(type(my_tuple))

#unpacking tuple
my_tuple1 = (12,34,5,43)
a,b,c,d = my_tuple1
print(a,b,c,d)
 
# concat tuple
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

concat_tuple = tuple1 + tuple2
print(concat_tuple)

# check key exist in tuple
my_tuple4 = (1, 2, 3, 4, 5)
key = 3

if key in my_tuple4:
    print("key exist")
else:
    print("key not exist")
    
# find index
my_tuple = (1, 2, 3, 4, 5)

index = my_tuple.index(5)
print(index)

            



    