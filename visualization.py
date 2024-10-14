import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(G):
    pos = nx.spring_layout(G)
    weights = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.show()
