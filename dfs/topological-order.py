class Node:
    def __init__(self,value):
        self.children=[]
        self.value=value
    # undirected graph
    def connect(self, node):
        self.children.append(node)

    def get_connections(self):
        print(f"node{self.value} connections", [node.value for node in self.children])
    
    def is_connected_to(self, node):
        return node in self.children


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def add_to_graph(self, node):
        self.nodes.append(node)
        
    def dfs(self, node, visited,ordering):
        if node in visited:
            return
        visited.add(node)
        # print("visiting Node", node.value)
        for child in node.children:
            self.dfs(child, visited, ordering)
        # about to pop values out
        ordering.insert(0, node.value)

    def topological_sort(self):
        ordering = []
        visited = set()
        for node in self.nodes:
            print(node.value)
            self.dfs(node, visited, ordering)
        return ordering

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

# add to graph
graph = Graph([e,b,c,d,a,f])
# connections
a.connect(b)
a.connect(c)
b.connect(d)
d.connect(f)
e.connect(c)
e.connect(f)

print(graph.topological_sort())