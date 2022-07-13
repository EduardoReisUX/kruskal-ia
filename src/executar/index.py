from convert_graph_data_type import convert
from busca_largura.index import bfs
from busca_profundidade.index import dfs
from kruskal.index import Graph

def executar_buscas_com_kruskal(graph: Graph, limit: int, grafo_op: str):
    # Executa algoritmo de kruskal
    dados_array_kruskal = graph.kruskal_algo(print_result=True)       
    
    # Converte os dados de list[list[int]] para dict
    dados_dict_kruskal = convert(dados_array_kruskal, print_results=False)
    
    # Executa a busca em largura
    print("\nResultado da busca em largura (ordem dos nós percorridos):")
    if grafo_op == "2":
        print(bfs(limit, dados_dict_kruskal, 2))
    else:
        print(bfs(limit, dados_dict_kruskal, 0))
    
    # Executa a busca em profundidade
    print("\nResultado da busca em profundidade (ordem dos nós percorridos):")
    if grafo_op == "2":
        print(dfs(limit, dados_dict_kruskal, 2, first_time=True))
    else:
        print(dfs(limit, dados_dict_kruskal, 0, first_time=True))
    
    input("\nAperte Enter para voltar pro começo...")


def executar_buscas_sem_kruskal(graph: Graph, limit: int, grafo_op: str): 
    dados_array = graph.get_graph(print_graph=True)    
    
    dados_dict = convert(dados_array, print_results=False)

    print("\nResultado da busca em largura (ordem dos nós percorridos):")
    if grafo_op == "2":
        print(bfs(limit, dados_dict, 1))
    else:
        print(bfs(limit, dados_dict, 0))
    
    print("\nResultado da busca em profundidade (ordem dos nós percorridos):")
    if grafo_op == "2":
        print(dfs(limit, dados_dict, 1, first_time=True))
    else:
        print(dfs(limit, dados_dict, 0, first_time=True))
    
    input("\nAperte Enter para voltar pro começo...")