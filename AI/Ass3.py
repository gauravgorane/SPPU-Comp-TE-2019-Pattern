
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Enter as many numbers as we want in the array and it will sort the numbers given below
             
arr = list(map(int, input("Enter space-separated numbers: ").split()))
selection_sort(arr)
print("Sorted array is:", arr)

# Output

# Enter space-separated numbers: 44 46 13 70 41
# Sorted array is: [13, 41, 44, 46, 70]


import sys
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
    def min_distance(self, dist, spt_set):
        min_dist = sys.maxsize
        min_index = 0
        for v in range(self.V):
            if dist[v] < min_dist and spt_set[v] == False:
                min_dist = dist[v]
                min_index = v
        return min_index
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        spt_set = [False] * self.V
        for cout in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and spt_set[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.print_solution(dist)
    def print_solution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])
V = int(input("Enter the number of vertices: "))
g = Graph(V)
print("Enter the adjacency matrix (space-separated entries, use 0 for no edge):")
for i in range(V):
    row = list(map(int, input().split()))
    g.graph[i] = row
src = int(input("Enter the source vertex: "))
g.dijkstra(src)

# Output

# Enter the number of vertices: 5        
# Enter the adjacency matrix (space-separated entries, use 0 for no edge):
# 0 5 6 3 2
# 1 0 7 4 9
# 8 4 0 6 2
# 3 7 5 0 1
# 8 7 3 6 0
# Enter the source vertex: 0
# Vertex  Distance from Source
# 0        0
# 1        5
# 2        5
# 3        3
# 4        2


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])
    def union(self, parent, rank, x, y):
        x_root = self.find_parent(parent, x)
        y_root = self.find_parent(parent, y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1
    def kruskal_mst(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        print("Edges in the constructed MST:")
        for u, v, weight in result:
            print("%d -- %d == %d" % (u + 1, v + 1, weight))
V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))
g = Graph(V)
print("Enter the edges as 'source destination weight':")
for i in range(E):
    u, v, w = map(int, input().split())
    g.add_edge(u - 1, v - 1, w)
g.kruskal_mst()

# Output

# Enter the number of vertices: 5
# Enter the number of edges: 5
# Enter the edges as 'source destination weight':
# 0 1 5
# 0 2 6
# 1 2 4
# 1 3 7
# 2 4 8
# Edges in the constructed MST:
# 1 -- 2 == 4
# 0 -- 1 == 5
# 1 -- 3 == 7
# 2 -- 4 == 8