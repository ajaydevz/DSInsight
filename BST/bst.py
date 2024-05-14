class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, node, key):
        if node is None: 
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)  
        elif key > node.key:
            node.right = self.insert(node.right, key)  

        return node  

    def inorder(self, root):
        if root:
            self.inorder(root.left)  
            print(root.key)
            self.inorder(root.right)  

    def preorder(self, root):
        if root:
            print(root.key)
            self.preorder(root.left)  
            self.preorder(root.right)  

    def postorder(self, root):
        if root:
            self.postorder(root.left)  
            self.postorder(root.right)  
            print(root.key)

    def delete_node(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete_node(root.left, key) 
        elif key > root.key:
            root.right = self.delete_node(root.right, key) 
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right

            root.key = self.minvalue_node(root.right)  

            root.right = self.delete_node(root.right, root.key)  

        return root

    def minvalue_node(self, root): 
        minvalue = root.key
        while root.left:
            minvalue = root.left.key
            root = root.left
        return minvalue

    def search(self, root, key):
        if root is None or root.key == key:  
            return root
        if key < root.key:
            return self.search(root.left, key) 
        return self.search(root.right, key)  
    
# Example usage
bst = BinaryTree()
root = None
keys = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for key in keys:
    root = bst.insert(root, key)

print("Inorder traversal:")
bst.inorder(root)
