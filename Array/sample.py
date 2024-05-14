class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        return f"hello, {self.name},{self.age}"
        


p = Person("ajay",23)
print(p.display())