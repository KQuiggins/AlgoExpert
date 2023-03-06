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