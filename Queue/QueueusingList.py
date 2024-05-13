class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self,item):
        self.items.append(item)
        
    def is_empty(self):
        return len(self.items) == 0
        
    def dequeu(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
        
    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]
        
    def size(self):
        return len(self.items)
        

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Queue:", q.items)  # Output: [1, 2, 3]

print("Dequeue:", q.dequeue())  # Output: 1
print("Queue:", q.items)  # Output: [2, 3]

print("Peek:", q.peek())  # Output: 2
print("Queue size:", q.size())  # Output: 2
        