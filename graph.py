import networkx as nx
import random

def create_transport_network():
    G = nx.Graph()
    
    places = ["A", "B", "C", "D", "E", "F", "G"]
    G.add_nodes_from(places)

    edges = [
        ("A", "B"), ("A", "C"), ("B", "D"),
        ("C", "D"), ("C", "E"), ("D", "E"),
        ("E", "F"), ("F", "G"), ("A", "G"),
        ("B", "F")
    ]

    for edge in edges:
        weight = random.randint(1, 10)
        G.add_edge(edge[0], edge[1], weight=weight)

    return G

def analyze_graph(G):
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degrees = dict(G.degree())

    print(f"Number of nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")
    print("Degree of vertices:")
    for node, degree in degrees.items():
        print(f"Vertex {node}: degree {degree}")
