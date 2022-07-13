# Algoritmo de Kruskal

class Graph:
    # Inicia o grafo com o número de nós definido na chamada.
    def __init__(self, vertices):
        self.num_vertices: int = vertices
        self.graph: 'list[list[int]]' = []    # [[0, 1, 4], [0, 2, 4], ...]

    # Add uma aresta no nó_1 e nó_2 de valor weight
    def add_edge(self, node_1: int, node_2: int, weight: int):
        self.graph.append([node_1, node_2, weight])

    # Retorna e printa o grafo sem executar o Kruskal
    def get_graph(self, print_graph = False):
        graph_result = []
        
        for node_1, node_2, weight in self.graph:
                graph_result.append([node_1, node_2, weight])

        if print_graph:
            print("Grafo: \n{nó_1} - {nó_2}: {peso}")
            for node_1, node_2, weight in graph_result:
                print(f"{node_1} - {node_2}: {weight}")
        
        """ print("mermaidjs:")
        for node_1, node_2, weight in graph_result:
            print(f"{node_1} -->|{weight}| {node_2}") """

        return graph_result

    # Procura, dentro da lista de parents, o index.
    def find(self, parent: 'list[int]', index: int):
        if parent[index] == index:
            return index

        return self.find(parent, parent[index])

    # Une 
    def apply_union(self, parent, rank, node_x, node_y):
        node_x_root = self.find(parent, node_x)
        node_y_root = self.find(parent, node_y)

        if rank[node_x_root] < rank[node_y_root]:
            parent[node_x_root] = node_y_root
        elif rank[node_x_root] > rank[node_y_root]:
            parent[node_y_root] = node_x_root
        else:
            parent[node_y_root] = node_x_root
            rank[node_x_root] += 1

    #  Executa algoritmo de Kruskal
    def kruskal_algo(self, print_result = False):
        result = []
        parent = []
        rank = []
        index, count = 0, 0

        # Ordena o grafo de acordo com o weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        for node in range(self.num_vertices):
            parent.append(node)     # parent =  [0, 1, 2, 3, 4, 5]
            rank.append(0)          # rank =    [0, 0, 0, 0, 0, 0]

        while count < self.num_vertices - 1:
            node_1, node_2, weight = self.graph[index]
            index = index + 1
            x = self.find(parent, node_1)
            y = self.find(parent, node_2)
            if x != y:
                count += 1
                result.append([node_1, node_2, weight])
                self.apply_union(parent, rank, x, y)

        if print_result:
            print("Resultado do algoritmo de Kruskal (árvore mínima): \n{nó_1} - {nó_2}: {peso}")
            for node_1, node_2, weight in result:
                print(f"{node_1} - {node_2}: {weight}")
            """ print("mermaidjs:")
            for node_1, node_2, weight in result:
                print(f"{node_1} --> |{weight}| {node_2}") """
            
        return result