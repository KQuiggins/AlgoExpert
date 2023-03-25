# Implementation of a Stack

```python

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

```

In this class, we define several methods that allow us to perform various operations on the stack.

## Initializing a Stack

```python
def __init__(self):
    self.items = []
```

The `__init__` method is called when we create a new instance of the `Stack` class. It initializes the `items` property to an empty list, which will hold the items in the stack.

## Checking if a Stack is Empty

```python

def is_empty(self):
    return len(self.items) == 0

```

The `is_empty` method checks if the stack is empty by checking if the `items` property has a length of 0.

## Pushing an Item onto the Stack

```python
def push(self, item):
    self.items.append(item)

```

The `push` method adds a new item to the top of the stack by appending it to the `items` property.

## Popping an Item off the Stack

```python

def pop(self):
    if self.is_empty():
        raise Exception("Stack is empty")
    return self.items.pop()

```

The `pop` method removes the top item from the stack by calling the `pop` method on the `items` property. However, before we do this, we check if the stack is empty. If it is, we raise an exception to let the user know that they can't pop an item off an empty stack.

## Peeking at the Top Item on the Stack

```python
def peek(self):
    if self.is_empty():
        raise Exception("Stack is empty")
    return self.items[-1]

```

The `peek` method returns the top item from the stack without removing it. We do this by accessing the last item in the `items` property. However, before we do this, we check if the stack is empty. If it is, we raise an exception to let the user know that they can't peek at an item on an empty stack.
