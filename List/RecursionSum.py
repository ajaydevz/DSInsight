def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)
        
arr = 6
print(recur_sum(arr))

arr= [1,2,3,4,5,6]

def arr_sum(arr,index=0):
    if len(arr) == index:
        return 0
    else:
        return arr[index] + arr_sum(arr,index+1)
        
print(arr_sum(arr))