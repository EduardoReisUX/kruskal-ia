import os
import platform
from kruskal.index import Graph
from convert_graph_data_type import convert
from busca_largura.index import bfs
from busca_profundidade.index import dfs

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Linux":
        os.system('clear')

def menu(graph: Graph, limit: int):
    op = None

    while op != "0":
        clear()

        if op == "1":
            dados_array = graph.get_graph(print_graph=True)[:]    
            dados_dict = convert(dados_array, print_results=False)

            print("\nResultado da busca em largura (ordem dos nós percorridos):")
            result_bfs = (bfs(limit, dados_dict, 0))[:]
            print(result_bfs)

            print("\nResultado da busca em profundidade (ordem dos nós percorridos):")
            result_dfs = (dfs(limit, dados_dict, 0))[:]
            print(result_dfs)

        elif op == "2":
            dados_array_kruskal = graph.kruskal_algo(print_result=True)[:]        # Executa algoritmo de kruskal
            dados_dict_kruskal = convert(dados_array_kruskal, print_results=False)

            print("\nResultado da busca em largura (ordem dos nós percorridos):")
            result_kruskal_bfs = (bfs(limit, dados_dict_kruskal, 0))[:]
            print(result_kruskal_bfs)

            print("\nResultado da busca em profundidade (ordem dos nós percorridos):")
            result_kruskal_dfs = (dfs(limit, dados_dict_kruskal, 0))[:]
            print(result_kruskal_dfs)
        
        print("\nMenu")
        print("1 - Executar buscas sem Kruskal ")
        print("2 - Executar buscas com Kruskal")
        print("0 - Sair")
        op = input()