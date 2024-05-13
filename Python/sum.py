# Write a recursive function to compute the sum of digits of a number.

arr = [1,2,3,4,5,6]

def sum_arr(arr,index=0):
    if len(arr) == index:
        return 0
    else:
        return arr[index] + sum_arr(arr,index+1)
        
print(sum_arr(arr))

# Write a  function to compute the sum of digits of a number.

total = 0
for i in arr:
    total += i
    
print(total)

print(sum(arr))
