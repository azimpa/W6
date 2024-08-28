from collections import deque

class Graph:
    def __init__(self):
        self.map = {}

    def insert(self, vertex, edge, direction):
        self.map.setdefault(vertex, [])
        self.map.setdefault(edge, [])
        self.connect(vertex, edge)
        if direction:
            self.connect(edge, vertex)

    def connect(self, vertex, edge):
        self.map[vertex].append(edge)

    def remove(self, vertex):
        self.map.pop(vertex, None)
        for edges in self.map.values():
            if vertex in edges:
                edges.remove(vertex)

    def bfs(self, start):
        queue = deque()
        visited = set()
        self.bfs_helper(start, queue, visited)

    def bfs_helper(self, start, queue, visited):
        queue.append(start)
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            edges = self.map[vertex]
            
            for element in edges:
                if element not in visited:
                    queue.append(element)
                    visited.add(element)
        
        if len(visited) < len(self.map):
            for key in self.map:
                if key not in visited:
                    start = key
                    break
            
            self.bfs_helper(start, queue, visited)
    
    def dfs(self, start):
        stack = []
        visited = set()
        self.dfs_helper(start, stack, visited)

    def dfs_helper(self, start, stack, visited):
        stack.append(start)
        visited.add(start)
        
        while stack:
            vertex = stack.pop()
            print(vertex, end=' ')
            edges = self.map[vertex]
            
            for element in edges:
                if element not in visited:
                    stack.append(element)
                    visited.add(element)
        
        if len(visited) < len(self.map):
            for key in self.map:
                if key not in visited:
                    start = key
                    break
            
            self.dfs_helper(start, stack, visited)
    
    def display(self):
        for key, value in self.map.items():
            print(f'{key}: {value}')

g = Graph()
g.insert(5, 6, False)
g.insert(8, 5, True)
g.insert(8, 7, True)
g.insert(7, 1, False)
g.insert(7, 5, False)
g.insert(6, 1, False)
g.insert(9, 2, False)
g.insert(4, 7, False)
g.insert(4, 10, False)
g.insert(10, 9, False)
g.insert(5, 11, False)
g.insert(11, 22, False)
g.remove(1)     
g.display()
print("bfs")
g.bfs(5)
print()
print("dfs")
g.dfs(9)
