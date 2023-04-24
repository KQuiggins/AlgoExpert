# Graph Data Structure

## Initializing a Graph

When a new graph object is created using the `Graph()` constructor, an empty dictionary is initialized in the `__init__` method:

```python
def __init__(self):
    self.adj_list = {}

```

This dictionary will hold the adjacency list for the graph. The keys in the dictionary will be the vertices of the graph, and the values will be lists of the vertices that are adjacent to the key vertex.

## Adding Edges to a Graph

The `add_edge` method adds a new edge to the graph. It takes two parameters, `vertex1` and `vertex2`, which are the vertices that the edge connects. If either of the vertices does not exist in the graph, it is added to the graph as a key in the `adj_list` dictionary with an empty list as its value. Then, the other vertex is appended to the list of adjacent vertices for the first vertex.

```python

def add_edge(self, vertex1, vertex2):
    if vertex1 not in self.adj_list:
        self.adj_list[vertex1] = []
    if vertex2 not in self.adj_list:
        self.adj_list[vertex2] = []
    self.adj_list[vertex1].append(vertex2)
    self.adj_list[vertex2].append(vertex1)

```

## Removing Edges from a Graph

The `remove_edge` method removes an edge from the graph. It takes two parameters, `vertex1` and `vertex2`, which are the vertices that the edge connects. If either of the vertices does not exist in the graph, an exception is raised. Then, the other vertex is removed from the list of adjacent vertices for the first vertex.

```python

def remove_edge(self, vertex1, vertex2):
    if vertex1 not in self.adj_list or vertex2 not in self.adj_list:
        raise Exception("Vertices not in graph")

```

## Removing a Vertex from a Graph

The `remove_vertex` method removes a vertex from the graph. It takes one parameter, `vertex`, which is the vertex to remove. If the vertex does not exist in the graph, an exception is raised. Then, the vertex is removed from the graph as a key in the `adj_list` dictionary. Finally, the vertex is removed from the list of adjacent vertices for all other vertices in the graph.

```python

def remove_vertex(self, vertex):
    if vertex not in self.adj_list:
        raise Exception("Vertex not in graph")
    for adjacent_vertex in self.adj_list[vertex]:
        self.adj_list[adjacent_vertex].remove(vertex)
    self.adj_list.pop(vertex)

```

## Depth First Search

The `dfs` method performs a depth-first search on the graph. It takes one parameter, `start`, which is the starting vertex for the search. It returns a list of the vertices that were visited during the search.

```python

def dfs(self, start):
    visited = []
    stack = Stack()
    stack.push(start)
    while not stack.is_empty():
        current_vertex = stack.pop()
        if current_vertex not in visited:
            visited.append(current_vertex)
            for adjacent_vertex in self.adj_list[current_vertex]:
                stack.push(adjacent_vertex)
    return visited

```

## Breadth First Search

The `bfs` method performs a breadth-first search on the graph. It takes one parameter, `start`, which is the starting vertex for the search. It returns a list of the vertices that were visited during the search.

```python

def bfs(self, start):
    visited = []
    queue = Queue()
    queue.enqueue(start)
    while not queue.is_empty():
        current_vertex = queue.dequeue()
        if current_vertex not in visited:
            visited.append(current_vertex)
            for adjacent_vertex in self.adj_list[current_vertex]:
                queue.enqueue(adjacent_vertex)
    return visited

```

## Using the Graph Class

The following code creates a new graph object and adds some edges to it:

```python

graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")


```

The following code performs a depth-first search on the graph, starting at vertex "A":

```python

print(graph.dfs("A"))

```

The following code performs a breadth-first search on the graph, starting at vertex "A":

```python

print(graph.bfs("A"))

```
