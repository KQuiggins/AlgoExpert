class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    if tree.value >= 0:
        return tree.value
    
    left = evaluateExpressionTree(tree.left)
    right = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return left + right
    if tree.value == -2:
        return left - right
    if tree.value == -3:
        return int(left / right)
    
   
    return left * right


# O(n) time | O(h) space
# where n is the number of nodes in the tree and h is the amount of space needed in stack for recursive calls
# base case is when we reach a leaf node