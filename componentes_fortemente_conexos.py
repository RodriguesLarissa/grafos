# DFS Componentes fortemente conexos
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

# DFS descrito por parenteses
tempo = 0
vertice_inicial = 0
vetor_entradas = [-1 for _ in range(quantidade_vertices)]
vetor_saidas = [-1 for _ in range(quantidade_vertices)]
dfs_parenteses = ""

def visitaDFS(vertice_analisado):
  global tempo
  global dfs_parenteses
  tempo += 1
  vetor_entradas[vertice_analisado] = tempo
  dfs_parenteses += f'({vertice_analisado} '
  for vertice in grafo_transposto[vertice_analisado]:
    if vetor_entradas[vertice] == -1:
      visitaDFS(vertice)
  tempo += 1
  vetor_saidas[vertice_analisado] = tempo
  dfs_parenteses += f'{vertice_analisado}) '

# Inicializa o DFS
for ordem in range(quantidade_vertices):
  if vetor_entradas[ordem] == -1:
    visitaDFS(ordem)

print(dfs_parenteses)