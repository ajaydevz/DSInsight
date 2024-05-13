def reverse_string(s):
    return s[::-1]
    
print(reverse_string('olleh'))

arr = [12,34,54,33,56,5]

def reverse_arr(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    return arr

print("reversed arr:",reverse_arr(arr))
    

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
        
print('factorial:',factorial(5))


def fibinacci(n):
    if n <= 1:
        return 1
    else:
        return fibinacci(n-1) + fibinacci(n-2)
        
m = 10

for i in range(m):
    print(fibinacci(i))
    
    
# binary tree

