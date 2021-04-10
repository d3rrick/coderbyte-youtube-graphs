# connections
# shortest routes
# nodes/vertices (x,y)
# edges (connections/lines)


# representation in code
# we are guided by space and time complexity

# list of vertices and edges

# vertices = ['A','B','C','D','E']
# edges = [
#     ['A','B'],
#     ['A','D'],
#     ['B','C'],
#     ['C','D'],
#     ['C','E'],
#     ['D','E'],
# ]

# Q.1= given a node, find all adjacent nodes
# time complexity - loop through edges array and search 
# 0(e)
# space - store array with all vertices(v) and another one for each one of them 0(e+v)
# Q.2 is there a connection between two nodes
# 0(e)


vertices = ['A','B','C','D','E']
edges = [
    ['A','B'],
    ['A','D'],
    ['B','C'],
    ['C','D'],
    ['C','E'],
    ['D','E'],
]

# Find all the adjacent nodes
def find_adjacent_nodes(node):
    # pseudo code
    # loop through edges
    # for each, is my node in the connection
    # if ok, push the other into the return array
    # if no keep looping
    # return array
    results=[]
    for sub_edge in edges:
        if node in sub_edge:
            pos = sub_edge.index(node)
            results += sub_edge[0:pos]+sub_edge[pos+1:]
    return results
# print(find_adjacent_nodes('C'))

def is_connected(node_x, node_y):
    # pseudo code
    # loop through edges and return if both are in same sub edges
    for sub_edge in edges:
        if node_x in sub_edge and node_y in sub_edge:
            return True
    return False
print(is_connected('A', 'E'))
