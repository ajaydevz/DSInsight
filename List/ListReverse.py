# Reverse a list without using built-in functions.

original_list = [1, 2, 3, 4, 5]

# inplace reverse 
def reverse_list(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    return arr
    
print(reverse_list(original_list))

# reverse not in inplace 
array = [1, 2, 3, 4, 5]
reversed_array = []

for i in range(len(array) -1,-1,-1):
    reversed_array.append(array[i])
    
print(reversed_array)

# reverse from middle
arr = [1, 2, 3, 4, 5, 6]
k = 3

def reverse_arr(arr,k):
    start = 0
    end = k - 1
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    return arr
    
print(reverse_arr(arr,k))
    
# The reverse() method reverses the elements of a list in place, it modify original list

original_list = [1, 2, 3, 4, 5]
original_list.reverse()
print(original_list)

# The reversed() function create new list without modify exisiting list

original_list = ['apple', 'banana', 'cherry']
reversed_list = list(reversed(original_list))
print(reversed_list)  # Output: ['cherry', 'banana', 'apple']





