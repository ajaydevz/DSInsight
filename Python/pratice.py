arr = [2,3,0,33,2,0,2,35,53,0]

for i in arr:
  if i == 0:
    arr.remove(i)
    arr.append(i)

print(arr)



arr1 = [23,44,54,32,65,42,36,43,22,15,7]
maximum = 0

for i in arr1:
  if i > maximum:
    maximum = i


print(maximum)


arr1 = [23,44,54,32,65,42,36,43,22,15,7]
minimum = arr1[0]
for i in arr1:
  if i < minimum:
    minimum = i
      

print(minimum)




def missingNumber(a):
    n = len(a)
    expected_sum = n * (n + 1) // 2
    actual_sum = 0
    for num in a:
        actual_sum += num
    return expected_sum - actual_sum

# Example usage:
arr = [3,2,0,4,1,5,7]
print(missingNumber(arr))  


