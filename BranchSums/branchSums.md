# Branch Sums

## Code Explanation

The code defines a class called `BinaryTree` with an `__init__` method that initializes an instance of the class with a `value`, `left`, and `right` attribute. The `value` attribute is set to the value passed into the `__init__` method, while the `left` and `right` attributes are set to `None` by default.

The code then defines a function called `nodeDepths` that takes a single argument, `root`, which represents the root of a binary tree. The function calls another function called `nodeDepthsHelper` with `root` and an initial `depth` of 0 as arguments, and returns the result of that function call.

The `nodeDepthsHelper` function is a recursive function that takes two arguments, `root` and `depth`. It initializes a variable called `runningTotal` to 0 and checks if `root` is `None`. If `root` is `None`, the function returns 0. Otherwise, it adds `depth` to `runningTotal`, and then recursively calls `nodeDepthsHelper` with `root.left` and `depth + 1` as arguments, and adds the result to `runningTotal`. It then recursively calls `nodeDepthsHelper` with `root.right` and `depth + 1` as arguments, and adds the result to `runningTotal`. Finally, it returns `runningTotal`.

The `nodeDepths` function essentially computes the sum of the depths of all nodes in a binary tree. The `nodeDepthsHelper` function is a recursive helper function that traverses the binary tree and keeps track of the current depth, adding it to the running total as it goes. The `nodeDepths` function simply calls `

## Code

```python
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root):
    # Write your code here.
    return nodeDepthsHelper(root, 0)

def nodeDepthsHelper(root, depth):
    runningTotal = 0
    if root is None:
        return 0
    else:
        runningTotal += depth
        runningTotal += nodeDepthsHelper(root.left, depth + 1)
        runningTotal += nodeDepthsHelper(root.right, depth + 1)
    
    return runningTotal
```

## Test 1

```python
tree = BinaryTree(1)
assert nodeDepths(tree) == 0
```

Explanation: This test creates a binary tree with a single node and asserts that the depth of the root node is 0, which is correct.

## Test 2

```python
tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.right = BinaryTree(3)
assert nodeDepths(tree) == 2
```

Explanation: This test creates a binary tree with three nodes and asserts that the sum of the depths of all nodes is 2, which is correct: the root node has a depth of 0, the left child has a depth of 1, and the right child has a depth of 1, for a total sum of 2.

## Test 3

```python
tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.right = BinaryTree(3)
tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(5)
tree.right.left = BinaryTree(6)
tree.right.right = BinaryTree(7)
print(assert nodeDepths(tree) == 10)
```

Explanation: This test creates a binary tree with seven nodes and asserts that the sum of the depths of all nodes is 10, which is correct: the root node has a depth of 0, the left child has a depth of 1, the right child has a depth of 1, the left child's left child has a depth of 2, the left child's right child has a depth of 2, the right child's left child has a depth of 2, the right child's right child has a depth of 2, for a total sum of 10
