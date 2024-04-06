class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
        
def preorder(root):
    if root:
        preorder(root.left)
        print(root.data, end=" ")
        preorder(root.right)
        
            

root = Node(10)
root.left = Node(20)
root.right = Node(34)
root.left.left = Node(45)
root.left.right = Node(50)

print('inorder traversel:')
preorder(root)
