
def evennum_gen(n):
    for i in range(0,n,2):
        yield i
        
for num in evennum_gen(10):
    print(num)
    

def shout(text):
    return text.upper()
    
print(shout('hello'))