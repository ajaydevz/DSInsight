# recursion using factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print('factorial 1 :',factorial(5))

# factorial without using recursion

def factoriall(n):
    if n <= 0:
        return n
    else:
        result = 1
        for i in range(1,n+1):
            result *= i
        return result

print('factorial 2 :',factoriall(10)) 

