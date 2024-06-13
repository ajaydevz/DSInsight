arr1 = [1,2,3,4,5]
arr2 = [4,5,6,7,8]
arr3 = arr1 + arr2

result = []
for i in arr3:
    if i not in arr2 or i not in arr1:
        result.append(i)
        
print(result)


name = "ajay dev"

words = name.split()

print(words)

reversed_1 = words[0][::-1]
reversed_2 = words[1][::-1]


reversed_each = [x[::-1] for x in words ]


print(reversed_each)




        
