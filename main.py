from graph import create_transport_network, analyze_graph
from algorithms import dfs_search, bfs_search, dijkstra
from visualization import visualize_graph

def main():
    transport_network = create_transport_network()
    
    analyze_graph(transport_network)
    print('\n')
    
    print("DFS:")
    dfs_search(transport_network)
    print('\n')

    print("BFS:")
    bfs_search(transport_network)
    print('\n')

    print('\nDijkstra:')
    print(dijkstra(transport_network, 'A'))

    visualize_graph(transport_network)

if __name__ == "__main__":
    main()
