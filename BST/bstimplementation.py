class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self,root):
        if root is None:
            return TreeNode(data)
        if data < root.data:
            root.left = insert(root.left, data)
        elif data > root.data:
            root.right = insert(root.right, data)
        return root
        
    def search(self,data):
        if root is None and root.data = data:
            return root
        if data < root.data:
            return search(root.left, data)
        else:
            return search(root.right, data)
        