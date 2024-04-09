class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("stack is empty")

    def size(self):
        return len(self.items)
    

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)

print(s.size())