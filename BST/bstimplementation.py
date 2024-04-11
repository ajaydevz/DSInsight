
class TreeNode:
  def __init__(self, data):
    self.right = None
    self.left = None
    self.data = data 

  def insert(root,data):
    if root is None:
      return TreeNode(data)

    if data < root.data:
      root.left = insert(root.left, data)

    elif data > root.data:
      root.right = insert(root.right, data)

    return root


  def search(root,value):
    if root is None and root.data == value:
      return root

    if root.data < value:
      return serach(root.left, value)
    else:
      return search(root.right, value)
