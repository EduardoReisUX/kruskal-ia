visited: list[int] = []     # Lista para acompanhar os nós visitados.
queue = []                  # Inicia uma fila

# Realizar busca em largura
def bfs(visited: list[int], graph: dict[list[int]], node: int = 0):
  result = []
  visited.append(node)
  queue.append(node)
  
  print("Resultado da busca em largura (ordem dos nós percorridos):", end="\t")

  while queue:
    s = queue.pop(0)
    result.append(s)

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

  print(result)
  return result
