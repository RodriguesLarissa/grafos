# Matriz de distancias

quantidade_vertices, quantidade_arcos = (int(tmp) for tmp in input().split(" "))
vetor_conexoes = [[] for _ in range(quantidade_vertices)]

for i in range(quantidade_arcos):
  vertice_origem, vertice_destino = (int(tmp) for tmp in input().split(" "))
  vetor_conexoes[vertice_origem].append(vertice_destino)

# Inicializa o BFS
for ordem in range(quantidade_vertices):
  fila = []
  grafo = [-1 for _ in range(quantidade_vertices)]
  grafo[ordem] = 0
  fila.append(ordem)

  while len(fila) != 0:
    vertice_analisado = fila[0];
    fila.pop(0)
    for vertice in vetor_conexoes[vertice_analisado]:
      if grafo[vertice] == -1:
        grafo[vertice] = grafo[vertice_analisado] + 1
        fila.append(vertice)

  conexao_str = ' '.join(map(str, grafo))
  print(f'{ordem}: {conexao_str}')