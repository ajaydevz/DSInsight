class Base1:
    def method_base1(self):
        return "method from base1"
    
class Base2:
    def method_base2(self):
        return "method from base2"
        
class Derived(Base1,Base2):
    def method_derived(self):
        return "method derived"
        
obj = Derived()

print(obj.method_base1())
print(obj.method_base2())
print(obj.method_derived())
    
    