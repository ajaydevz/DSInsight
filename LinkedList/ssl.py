class Node:
    def__init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def__init__(self):
        self.head = None
        
    def insert(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def delete(self,data):
        if self.head is None:
            return 
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            current_node.next = current.node.next.next
            return
        current_node = current_node.next
        
    def search(self,data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
        
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end"=>")
            current_node = current_node.next
        
        
    
            
