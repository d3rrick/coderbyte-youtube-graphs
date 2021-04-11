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

    
    def shortest_path(self, start, end):
        visited= {}
        if start is None:
            return results
        queue=[start]
        visited[start.value]= None
        while queue:
            current = queue.pop(0)
            if current.value == end.value:
                return self.reconstruct(visited, start.value, end.value)
            for child in current.children:
                if not child.value in visited:
                    visited[child.value] = current.value
                    queue.append(child)
# friends connections,
# find the shotest connection between two friends
Hannah = Node("Hannah")
Mary = Node("Mary")
Mel = Node("Mel")
Max = Node("Max")
Dan = Node("Dan")
Nis = Node("Nis")
Chris = Node("Chris")
Nicole = Node("Nicole")
Yair = Node("Yair")
Mabel = Node("Mabel")
Liz = Node("Liz")
# add to graph
graph = Graph([Hannah,Mary,Mel,Dan,Nis ,Chris,Nicole,Yair,Mabel,Liz])
# connections
Hannah.connect(Mary)
Hannah.connect(Mel)
Hannah.connect(Max)
Hannah.connect(Liz)
Hannah.connect(Nis)
Nis.connect(Dan)
Nis.connect(Chris)
Nis.connect(Yair)
Yair.connect(Mabel)
Yair.connect(Liz)
Yair.connect(Chris)
Mabel.connect(Liz)
Chris.connect(Nicole)
Mel.connect(Max)

print(graph.shortest_path(Hannah, Yair)) #Hannah=>Liz=>Yair
print(graph.shortest_path(Nicole, Dan)) #Nicole=>Chris=>Nis=>Dan
print(graph.shortest_path(Nis, Mabel)) #Nis=>Yair=>Mabel
print(graph.shortest_path(Max, Liz)) #Max=>Hannah=>Liz
print(graph.shortest_path(Nis, Mel)) #Nis=>Hannah=>Mel
print(graph.shortest_path(Hannah,Hannah)) #Hannah
