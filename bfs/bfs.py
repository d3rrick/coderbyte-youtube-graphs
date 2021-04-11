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
    
    def reconstruct(self,visited, start,end):
        final= []
        running = end
        while running:
            final.insert(0,running)
            running = visited[running]
        return "=>".join(final)
    
    def bfs(self, node):
        visited=set()
        results=[]
        if node is None:
            return results
        queue=[node]
        # add the first element to visited set
        visited.add(node)
        while queue:
            current = queue.pop(0)
            results.append(current.value)
            for child in current.children:
                if not child in visited:
                    queue.append(child)
                    visited.add(child)
        return results


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

# add to graph
graph = Graph([DFW,JFK,LAX,HNL,SAN,EWR,BOS,MIA,MCO,PBI])

# connections
DFW.connect(LAX)
DFW.connect(JFK)
LAX.connect(HNL)
LAX.connect(EWR)
LAX.connect(SAN)
JFK.connect(BOS)
JFK.connect(MIA)
MIA.connect(MCO)
MCO.connect(PBI)
MIA.connect(PBI)
   
# bfs
print(graph.bfs(BOS))

# complexity
# O(v+e)
# space o(v)