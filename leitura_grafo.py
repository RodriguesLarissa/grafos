# Coleta de vertices e arcos de grafos
quantidade_vertices, quantidade_arcos = (int(tmp) for tmp in input().split(" "))
vetor_conexoes = [[] for _ in range(quantidade_vertices)]

for i in range(quantidade_arcos):
  vertice_origem, vertice_destino = (int(tmp) for tmp in input().split(" "))
  vetor_conexoes[vertice_origem].append(vertice_destino)

for index, vertice in enumerate(vetor_conexoes):
  conexao_str = ' '.join(map(str, vetor_conexoes[index]))
  print(f'{index}: {conexao_str}')