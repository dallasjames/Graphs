"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        else:
            print("Already in there")

    def add_edge(self, v1, v2):
        if v1 and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("Vertex doesn't exist")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        queue = Queue()
        visited = set()
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            current = queue.dequeue()
            if current not in visited:
                print(current)
                visited.add(current)
                for i in self.get_neighbors(current):
                    queue.enqueue(i)

    def dft(self, starting_vertex):
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            current = stack.pop()
            if current not in visited:
                print(current)
                visited.add(current)
                for i in self.get_neighbors(current):
                    stack.push(i)

    def dft_recursive(self, starting_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for i in self.vertices[starting_vertex]:
            if i not in visited:
                self.dft_recursive(i, visited)

    def bfs(self, starting_vertex, destination_vertex):
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()
        while queue.size() > 0:
            path = queue.dequeue()
            current = path[-1]
            if current not in visited:
                if current == destination_vertex:
                    return path
            visited.add(current)
            for i in self.vertices[current]:
                new_path = list(path)
                new_path.append(i)
                queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        while stack.size() > 0:
            path = stack.pop()
            current = path[-1]
            if current not in visited:
                if current == destination_vertex:
                    return path
            visited.add(current)
            for i in self.vertices[current]:
                new_path = list(path)
                new_path.append(i)
                stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        for i in self.vertices[starting_vertex]:
            if i not in visited:
                new_path = self.dfs_recursive(i, destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None

    def earliest(self, starting_vertex):
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        longest_path = [starting_vertex]
        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]
            if vertex not in visited:
                visited.add(vertex)
                for i in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(i)
                    stack.push(new_path)
                    if len(new_path) > len(longest_path):
                        longest_path = new_path
                    if len(new_path) == len(longest_path) and new_path[-1] != longest_path[-1]:
                        longest_path = new_path
        return longest_path
