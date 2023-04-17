def findClosestValueInBst(tree, target):
    closest = tree.value

    while tree is not None:
        if abs(tree.value - target) < abs(closest - target):
            closest = tree.value
        if closest == target:
            break
        if tree.value > target:
            tree = tree.left
        else:
            tree = tree.right
    return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None