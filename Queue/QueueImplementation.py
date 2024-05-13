class Queue:
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return len(self.queue) == 0
        
    def enqueue(self,item):
        self.queue.append(item)
        
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return None
        else:
            self.queue.pop(0)
            
    def peek(self):
        if self.is_empty():
            print("queue is empty")
        else:
            return self.queue[0]
            
    def display(self):
        if self.is_empty():
            print("queue is empty")
            return 
        for i in self.queue:
            print(i, end=" ")
        print()
        
        
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.display()  # Output: 1 2 3 4 5
q.dequeue()  # Output: 1
print("Peek:", q.peek())  # Output: 2
q.display() 