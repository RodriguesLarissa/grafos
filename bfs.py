# BFS
fila = []
quantidade_vertices, quantidade_arcos, vertice_inicial = (int(tmp) for tmp in input().split(" "))
vetor_conexoes = [[] for _ in range(quantidade_vertices)]
grafo = [-1 for _ in range(quantidade_vertices)]

for i in range(quantidade_arcos):
  vertice_origem, vertice_destino = (int(tmp) for tmp in input().split(" "))
  vetor_conexoes[vertice_origem].append(vertice_destino)

# Inicializa o BFS
grafo[vertice_inicial] = 0
fila.append(vertice_inicial)

while len(fila) != 0:
  vertice_analisado = fila[0];
  fila.pop(0)
  for vertice in vetor_conexoes[vertice_analisado]:
    if grafo[vertice] == -1:
      grafo[vertice] = grafo[vertice_analisado] + 1
      fila.append(vertice)

conexao_str = ' '.join(map(str, grafo))
print(f'{vertice_inicial}: {conexao_str}')