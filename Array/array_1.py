# Find maximum element in array ?

array = [15,43,23,56,32,67,34]

max_element = 0

for i in range(len(array)):
    if array[i] > max_element:
        max_element = array[i]

print(max_element)  #67

# using built-in method 

print(max(array))  #67
 
# Find minimum element in array ?