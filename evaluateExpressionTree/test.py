from evaluateExpressionTree import BinaryTree, evaluateExpressionTree



# Test Case 1
tree1 = BinaryTree(3)
assert evaluateExpressionTree(tree1) == 3

# Test Case 2
tree2 = BinaryTree(-1, BinaryTree(2), BinaryTree(4))
assert evaluateExpressionTree(tree2) == 6

# Test Case 3
tree3 = BinaryTree(-2, BinaryTree(5), BinaryTree(3))
assert evaluateExpressionTree(tree3) == 2

# Test Case 4
tree4 = BinaryTree(-3, BinaryTree(10), BinaryTree(2))
assert evaluateExpressionTree(tree4) == 5

# Test Case 5
tree5 = BinaryTree(-2, BinaryTree(-1, BinaryTree(2), BinaryTree(1)), BinaryTree(4))
assert evaluateExpressionTree(tree5) == -3
