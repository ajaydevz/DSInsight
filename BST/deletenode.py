# delete node in bst

class TreeNode:
  def __init__(self,value) -> None:
    self.left = None
    self.right = None
    self.value = value

  def delete_node(root,key):
    if root is None:
      return root

    if key > root.value:
      root.left = delete_node(root.left, key)
    elif key < root.value:
      root.right = delete_node(root.right, key)

    else:
      # root with one child
      if root.left is None:
        temp = root.right
        root = None
        return temp

      elif root.right is None:
        temp = root.right:
        root  = None
        return temp