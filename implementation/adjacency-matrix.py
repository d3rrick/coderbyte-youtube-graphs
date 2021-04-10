# we use 2d lists
# both x and y represent edges
# if there is a connection we mark 1 else 0
# A -> B
# A -> D
# B -> C
# C -> D
# C -> E
# D -> E

# vertices = ['A','B','C','D','E']
# matrix = [
#     [0,1,0,1,0],
#     [1,0,1,0,0],
#     [0,1,0,1,1],
#     [1,0,1,0,1],
#     [0,0,1,1,0],
# ]
# time complexity 0(v) 
# checking connection - constant time
# space - all the possible edges have to stored, grows in x and y axis
# growth is exponential
# for undirected graph, then the matrix is symetric around the diagonal 

vertices = ['A','B','C','D','E']
matrix = [
    [0,1,0,1,0],
    [1,0,1,0,0],
    [0,1,0,1,1],
    [1,0,1,0,1],
    [0,0,1,1,0],
]
# Find all the adjacent nodes
def find_adjacent_nodes(node):
    results = []
    if node not in vertices:
        return ValueError("Node not found!")
    sub_edge_idx = vertices.index(node)
    sub_edge = matrix[sub_edge_idx]
    for idx in range(len(sub_edge)):
        if sub_edge[idx]: #1 is truthy
            # if 1 then append the value in vertices at that idx
            results.append(vertices[idx])
    return results

print(find_adjacent_nodes('C')) #['B', 'D', 'E']
print(find_adjacent_nodes('A')) #['B', 'D']
print(find_adjacent_nodes('K')) #[]

def is_connected(node_x, node_y):
    node_x_idx = vertices.index(node_x)
    node_y_idx = vertices.index(node_y)
    if matrix[node_x_idx][node_y_idx] and matrix[node_y_idx][node_x_idx]:
        return True
    return False

assert is_connected('A','B')
assert is_connected('A','D')
assert is_connected('B','C')
assert is_connected('C','D')
assert is_connected('C','E')
assert is_connected('D','E')
assert is_connected('A','E')
