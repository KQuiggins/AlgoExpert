# Tutorial: Binary Search Trees

Hey there! Today we're going to learn about binary search trees, or BSTs for short. A BST is a data structure that is used to efficiently store and retrieve data in sorted order.

## What is a Binary Search Tree?

A binary search tree is a tree data structure where each node has at most two children, referred to as the left child and the right child. The left child is always less than the parent, and the right child is always greater than the parent.

Here's an example of a simple binary search tree:

```python
     5
    / \
   2   8
  /
 14

```

As you can see, each node has at most two children, and the left child is always less than the parent and the right child is always greater than the parent.

## Inserting into a BST

To insert a new node into a BST, we start at the root node and compare the value we want to insert to the value of the current node. If the value is less than the current node, we move to the left child. If the value is greater than the current node, we move to the right child. We continue this process until we reach a leaf node (i.e., a node with no children), at which point we insert the new node as the left or right child of the leaf node, depending on whether it is less than or greater than the leaf node.

Here's some pseudocode to illustrate the process:

```python

function insert(node, value):
    if node is null:
        return new Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)

    return node

```

## Searching in a BST

To search for a value in a BST, we start at the root node and compare the value we're looking for to the value of the current node. If the value is less than the current node, we move to the left child. If the value is greater than the current node, we move to the right child. We continue this process until we find the node with the value we're looking for, or until we reach a leaf node and determine that the value is not in the tree.

Here's some pseudocode to illustrate the process:

```python

function search(node, value):
    if node is null or node.value == value:
        return node

    if value < node.value:
        return search(node.left, value)
    else:
        return search(node.right, value)

```

## Conclusion

That's it for the basics of binary search trees! With this knowledge, you should be able to create your own BST and insert and search for values in it. Of course, there's a lot more to learn about BSTs, such as deleting nodes and re=balancing the tree to maintain its efficiency, but that's beyond the scope of this tutorial.

Thanks for reading, and happy coding!
