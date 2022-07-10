from auxiliar.clear_terminal import clear_terminal
from executar.index import executar_buscas_com_kruskal, executar_buscas_sem_kruskal
from grafos.index import get_graph_1, get_graph_2

def menu(limit: int):
    kruskal_op = grafo_op = None

    while kruskal_op != "0":
        clear_terminal()
        
        print("Selecione um grafo de exemplo:")
        print("1 - Grafo 1")
        print("2 - Grafo 2")
        print("0 - Sair")

        grafo_op = input()

        if (grafo_op == "1"):
            graph = get_graph_1()
        elif (grafo_op == "2"):
            graph = get_graph_2()
        elif (grafo_op == "0" or grafo_op != "1" or grafo_op != "2"):
            return

        print("\nSelecione se deseja executar sem ou com o algoritmo de Kruskal:")
        print("1 - Executar buscas sem Kruskal ")
        print("2 - Executar buscas com Kruskal")
        print("0 - Sair")

        kruskal_op = input()
        print()

        if kruskal_op == "1":
            executar_buscas_sem_kruskal(graph, limit, grafo_op)
        elif kruskal_op == "2":
            executar_buscas_com_kruskal(graph, limit, grafo_op)