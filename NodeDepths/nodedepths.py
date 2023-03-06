

def nodeDepths(root):
   sum = 0
   return nodeDepthHelper(root, sum)


def nodeDepthHelper(root, sum, depth=0):
    if root is None:
        return sum
    else:
        sum += depth
        sum = nodeDepthHelper(root.left, sum, depth + 1)
        sum = nodeDepthHelper(root.right, sum, depth + 1)

    return sum
    
    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None