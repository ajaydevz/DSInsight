# fibonacci using recursion

def fibanacci(n):
    if n <= 1:
        return n
    else:
        return fibanacci(n-1) + fibanacci(n-2)

n = 20

for i in range(n):
    print(fibanacci(i))


# Implement Fibonacci sequence using recursion.

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
        
def fib_series(n):
    series=[]
    for i in range(n):
        series.append(fib(i))
    return series

# Implement Fibonacci sequence without using recursion.

def fib_ser(n):
    fib_arr = [0,1]
    for i in range(2,n):
        fib_arr.append(fib_arr[i-1] + fib_arr[i-2])
    return fib_arr
    
print(fib_ser(15))
print(fib(10))
print(fib_series(10))



