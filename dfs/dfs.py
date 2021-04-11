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
    def __init__(self, nodes):
        self.nodes = nodes

    def add_to_graph(self, node):
        self.nodes.append(node)
    
    def depth_first_traversal(self,start,end, visited=set()):
        # keep traversing deeply
        # until you hit the leaf node
        # or you are at the end
        if start.value == end.value:
            print(start.value)
            print("Found!")
            return
        print("Visiting Node",start.value)
        visited.add(start.value)
        for child in start.children:
            if not child.value in visited:
                self.depth_first_traversal(child, end, visited)
        

DFW = Node("DFW")
JFK = Node("JFK")
LAX = Node("LAX")
HNL = Node("HNL")
SAN = Node("SAN")
EWR = Node("EWR")
BOS = Node("BOS")
MIA = Node("MIA")
MCO = Node("MCO")
PBI = Node("PBI")
HKG = Node("HKG")

# add to graph
graph = Graph([DFW,JFK,LAX,HNL,SAN,EWR,BOS,MIA,MCO,PBI,HKG])

# connections
DFW.connect(LAX)
DFW.connect(JFK)
LAX.connect(HNL)
LAX.connect(EWR)
LAX.connect(SAN)
SAN.connect(HKG)
JFK.connect(BOS)
JFK.connect(MIA)
MIA.connect(MCO)
MCO.connect(PBI)
MIA.connect(PBI)
# bfs
print(graph.depth_first_traversal(DFW,PBI))

# complexity
# O(v+e) -  we are visiting all vertices
# space o(v) - the visited array will store at most each vertex if we traverse the entire graph

# uses
# - detecting cycle
# - detect bipartite
# - find if there is a path between nodes
# - topological sort

