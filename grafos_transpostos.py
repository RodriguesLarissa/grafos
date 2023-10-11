# Grafos transpostos
quantidade_vertices, quantidade_arcos = (int(tmp) for tmp in input().split(" "))
vetor_conexoes = [[] for _ in range(quantidade_vertices)]
grafo_transposto = [[] for _ in range(quantidade_vertices)]

for i in range(quantidade_arcos):
  vertice_origem, vertice_destino = (int(tmp) for tmp in input().split(" "))
  vetor_conexoes[vertice_origem].append(vertice_destino)

for index, vertice in enumerate(vetor_conexoes):
  for conexao in vertice:
    grafo_transposto[conexao].append(index)

for index, vertice in enumerate(grafo_transposto):
  conexao_str = ' '.join(map(str, grafo_transposto[index]))
  print(f'{index}: {conexao_str}')