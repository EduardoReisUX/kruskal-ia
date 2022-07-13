

# Realizar busca em largura
def bfs(limit: int, graph: 'dict[list[int]]', node: int = 0):
  queue = []    # Inicia uma fila
  count = 1
  result = []
  queue.append(node)

  while queue and count < limit:
    s = queue.pop(0)
    count = count + 1
    result.append(s)

    for neighbour in graph[s]:
      queue.append(neighbour)

  if count >= limit:
    print("Limite de buscas atingido.")
    return result
  
  return result
