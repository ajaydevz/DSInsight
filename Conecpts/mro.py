class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

# Creating an instance of D
d = D()

# Calling the show method
d.show()

# Printing the MRO of class D
print(D.__mro__)
print(D.mro())
