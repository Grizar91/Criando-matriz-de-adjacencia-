import networkx as nx
import numpy as np

def create_adjacency_matrix(file_path):
    G = nx.DiGraph()  # Grafo direcionado

    # Lê o arquivo de texto e adiciona as arestas ao grafo
    with open(file_path, "r") as file:
        for line in file:
            source, target = line.strip().split()
            G.add_edge(source, target)

    # Obtém a lista de nós (vértices) no grafo
    nodes = list(G.nodes())
    
    # Cria uma matriz de adjacência usando a lista de nós
    adjacency_matrix = np.zeros((len(nodes), len(nodes)), dtype=int)

    for source_index, source_node in enumerate(nodes):
        for target_index, target_node in enumerate(nodes):
            if G.has_edge(source_node, target_node):
                adjacency_matrix[source_index, target_index] = 1

    return adjacency_matrix, nodes

# Caminho para o arquivo de texto contendo as arestas
file_path = "graph.txt"

adjacency_matrix, nodes = create_adjacency_matrix(file_path)

print("Matriz de Adjacência:")
print(adjacency_matrix)

print("\nLista de Nós:")
print(nodes)
