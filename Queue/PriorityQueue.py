import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
        
    def enqueue(self,priority,item):
        heapq.heappush(self.items,(priority,item))
        
    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.items)[1]
        else:
            print("queue is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.elements[0][1]
        else:
            print("pq is empty")
        
    def __str__(self):
        """Return a string representation of the priority queue."""
        return str([item for item in self.items])

            

pq = PriorityQueue()
pq.enqueue('task1', 3)
pq.enqueue('task2', 1)
pq.enqueue('task3', 2)
print(pq)


            

    