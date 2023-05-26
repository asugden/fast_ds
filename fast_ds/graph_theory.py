import matplotlib.pyplot as plt
import networkx as nx

nodes = list(range(10))
edges = [(1, 0), (2, 1), (3, 2), (4, 1), (5, 0),
         (0, 5), (6, 3), (7, 3), (3, 0), (8, 0), (9, 8)]

gx = nx.DiGraph()
gx.add_nodes_from(nodes)
gx.add_edges_from(edges)

# pr = nx.pagerank(gx, max_iter=1000)
# print(pr)

# Plotting, complicatedly
# pos = nx.spring_layout(gx)
# nx.draw_networkx_nodes(gx, pos=pos, node_size=[pr[node]*300 for node in nodes])
# nx.draw_networkx_edges(gx, pos=pos)
# plt.show()

# Connected components
first_gx = nx.Graph()
first_gx.add_nodes_from(nodes)
first_gx.add_edges_from(edges)
comp = nx.connected_components(first_gx)

# If the length of the connected component is 1, don't use pagerank
# If it's 2, don't use pagerank, pick the parent
# If it's > 2, use pagerank
print(list(comp))