def fibinocci():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b
        
gen_fib = fibinocci()

for i in range(25):
    print(next(gen_fib))
    