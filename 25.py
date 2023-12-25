from networkx import Graph, minimum_edge_cut, connected_components

with open("input/25.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    
nodes = set()
edges = set()

for line in lines:
    node, connections = line.split(": ")
    nodes.add(node)
    connections = connections.split(" ")
    for connection in connections:
        edges.add(tuple(sorted([node, connection])))
        

G = Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

edges_to_cut = minimum_edge_cut(G)

for edge in edges_to_cut:
    G.remove_edge(*edge)
    
components = [len(c) for c in connected_components(G)]
product = 1
for c in components:
    product *= c
print(product)