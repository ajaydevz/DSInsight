class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,item):
        self.stack.append(item)
        
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
        
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
        
    def is_empty(self):
        return len(self.stack) == 0
        
    def size(self):
        return len(self.stack)
        
        
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.stack)
print("Size:", stack.size())
print("Peek:", stack.peek())

popped_item = stack.pop()
print("Popped item:", popped_item)
print("Stack after popping:", stack.stack)
print("Size after popping:", stack.size())