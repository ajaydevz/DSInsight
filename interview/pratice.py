class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def intro_yourself(self):
        return f"my name is {self.name} and my age is {self.age}"
        

p1 = Person('aswin',23)
p2 = Person('ali',22)
print(p2.intro_yourself())
print(p1.intro_yourself())

p1.age = 24
p1.name = 'dammu'
print(p1.intro_yourself())


numbers = [1,2,3,4,5]
doubles_num = map(lambda x:x*2 , numbers)
print(list(doubles_num))

month = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'] 
print(month)
convert_list = tuple(month)
print(convert_list)




