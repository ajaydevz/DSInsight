class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next 
            current.next = prev
            prev = current
            current = next
        self.head = prev

    
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next  = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while temp :
            print(temp.data, end=" ")
            temp = temp.next


l1 = Linkedlist()
l1.push(10)
l1.push(20)
l1.push(30)
l1.push(50)

print("given linked list:")
l1.printlist()

print("\nthe given linkedlist after reversing:")
l1.reverse()
l1.printlist()

    
    
