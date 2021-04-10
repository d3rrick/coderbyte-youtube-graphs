# time complexity = 0(1)
# stores list of vertices

# check if two nodes are connected 0(log(v)) assuming they are sorted
# space 0(e) the max will be the max no of edges

vertices = ['A','B','C','D','E']
# edges = [
#     ['B','D'],
#     ['A','C'],
#     ['B','D','E'],
#     ['A','C','E'],
#     ['C','D'],
# ]
class Node:
    def __init__(self,value):
        self.children=[]
        self.value=value
    # undirected graph
    def connect(self, node):
        # append two ways
        self.children.append(node)
        node.children.append(self)

    def get_connections(self):
        print(f"node{self.value} connections", [node.value for node in self.children])
    
    def is_connected_to(self, node):
        return node in self.children and self in node.children


class Graph:
    def __init__(self, *node):
        self.nodes = list(node)

    def add_to_graph(self, node):
        self.nodes.append(node)
    
 

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")

# add to graph
graph = Graph(nodeA,nodeB,nodeC,nodeD,nodeE)
graph.add_to_graph(nodeF)
# print([g.value for g in graph.nodes])

# connections
# A -> B
# A -> D
# B -> C
# C -> D
# C -> E
# D -> E
nodeA.connect(nodeB)
nodeA.connect(nodeD)
nodeB.connect(nodeC)
nodeC.connect(nodeD)
nodeC.connect(nodeE)
nodeD.connect(nodeE)
   
# print connections
nodeA.get_connections()
nodeB.get_connections()
nodeC.get_connections()
nodeD.get_connections()
nodeE.get_connections()

# test is_connected
print(nodeA.is_connected_to(nodeB)) #True
print(nodeA.is_connected_to(nodeC)) #False
print(nodeB.is_connected_to(nodeA)) #True
print(nodeA.is_connected_to(nodeE)) #False
print(nodeC.is_connected_to(nodeE)) #True
