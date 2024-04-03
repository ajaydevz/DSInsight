# here is the way revrse an array with less complexity!

arr = [1,23,44,53,90,32,45,23]

n = len(arr)
for i in range(n // 2):
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]

print(arr)

# reversing using slicing technique

arr1 = [12,45,32,54,23,64,32,53]

print(arr1[::-1])

# using reversed function

arr2 = [34,56,42,45,32,67,65]

reverse_arr = reversed(arr2)
print(list(reverse_arr))