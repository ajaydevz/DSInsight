# Find the largest,second largest number in a list.

numbers = [10, 20, 4, 45, 99]

largest = 0
for i in numbers:
    if i > largest:
        largest = i
        
print(largest)

def second_largest(arr):
    largest = 0
    second_largest = 0
    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i
    return second_largest
    
print(second_largest(numbers))