# fibonacci using recursion

def fibanacci(n):
    if n <= 1:
        return n
    else:
        return fibanacci(n-1) + fibanacci(n-2)

n = 20

for i in range(n):
    print(fibanacci(i))




