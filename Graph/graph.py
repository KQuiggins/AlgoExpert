class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list:
            self.adj_list[vertex1] = []
        if vertex2 not in self.adj_list:
            self.adj_list[vertex2] = []
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list or vertex2 not in self.adj_list:
            raise Exception("Vertices not in graph")
        if vertex2 in self.adj_list[vertex1]:
            self.adj_list[vertex1].remove(vertex2)
            self.adj_list[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        if vertex not in self.adj_list:
            raise Exception("Vertex not in graph")
        for neighbor in self.adj_list[vertex]:
            self.adj_list[neighbor].remove(vertex)
        del self.adj_list[vertex]

        # Remove the vertex from the list of vertices
        for v in list(self.adj_list.keys()):
            if v == vertex:
                del self.adj_list[v]

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_helper(start_vertex, visited)
        return visited

    def _dfs_helper(self, curr_vertex, visited):
        visited.add(curr_vertex)
        print(curr_vertex)
        for neighbor in self.adj_list[curr_vertex]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = []
        visited.add(start_vertex)
        queue.append(start_vertex)
        while queue:
            curr_vertex = queue.pop(0)
            print(curr_vertex)
            for neighbor in self.adj_list[curr_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited



# Create a new graph object
g = Graph()

# Add some vertices to the graph
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)

# Add some edges to the graph
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)

# Remove an edge from the graph
g.remove_edge(1, 2)

# Remove a vertex from the graph
g.remove_vertex(4)

# Perform a depth-first search of the graph
dfs_result = g.dfs(1)
print("Depth-First Search Result:", dfs_result)

# Perform a breadth-first search of the graph
bfs_result = g.bfs(1)
print("Breadth-First Search Result:", bfs_result)
