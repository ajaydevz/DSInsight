# implementations of singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next

sll = SinglyLinkedList()
sll.append(55)
sll.append(65)
sll.append(57)
sll.append(75)

sll.display()

print(type(sll))