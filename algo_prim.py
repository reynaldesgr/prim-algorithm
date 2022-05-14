
from heapq import heappop, heappush


class MinHeap:
    # Constructor to initialize a heap
    def __init__(self):
        self.heap = [] 
  
    def parent(self, i):
        return (i-1)/2
      
    # Inserts a new key 'k'
    def insertKey(self, k, v):
        heappush(self.heap, (k, v))           
  
    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self, i, new_val):
        self.heap[i]  = new_val 
        while(i != 0 and self.heap[self.parent(i)][1] > self.heap[i][1]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i] , self.heap[self.parent(i)] = (
            self.heap[self.parent(i)], self.heap[i])
              
    # Method to remove minium element from min heap
    def extractMin(self):
        return heappop(self.heap)
    def edges(self):
        L = []
        for u in self.heap:
            L.append(u[0])
        return L

        

def create_weighted_graph(path, n):
    graph = {}
    edges = []
    with open(path, "r") as f:
        for line in f:
            data = list(line.strip().split(":"))
            for u in range(1, len(data), 2):
                edges.append((data[u], int(data[u+1])))
            graph[data[0]] = edges
            edges = []
    return graph

def are_linked(graph, x, y):
    for s in graph[x]:
        if(s[0] == y):
            return True
    return False 

def min_(graph, s, E):
   t   = None
   w = graph.get(s)
   p = []
   for x in range(0, len(w)):
        if(w[x][0] not in E):
            p.append((w[x][0], w[x][1]))
   p.sort(key=lambda x:x[1])
   return p[0][0] if p != [] else None

def prim(graph, r):
    keys   = {}
    parent = {}
    for u in graph.keys():
        keys[u]   = float("inf")
        parent[u] = "NIL"

    E = MinHeap()
    keys[r] = 0
    E.insertKey(r, keys[r])
    for u in graph.keys():
            if(u!=r):
                E.insertKey(u, keys[u])
    while len(E.heap) != 0:
        u = E.extractMin()
        for v in graph[u[0]]:
            if(v[0] in E.edges() and keys.get(v[0]) > v[1]):
                parent[v[0]] = u[0]
                keys[v[0]]   = v[1]
    return parent

graph = create_weighted_graph("test.txt", 4);
print(prim(graph,'a'))
