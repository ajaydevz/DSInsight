
# global private and protect variable

global_Ar = 10

def func():

    global global_Ar
    global_Ar = 20


func()
print(global_Ar)

