# bst implementation

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key 
        
        
def insert(node,key):
    if Node is None:
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    
    return node

    
def search(root,key):
    if root is None and root.key == key:
        return root
        
    if root.key < key:
        return search(root.right, key)
    elif root.key > key:
        return search(root.left, key)
        
            