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
finalizacoes = []
vetor_entradas = [-1 for _ in range(quantidade_vertices)]
vetor_saidas = [-1 for _ in range(quantidade_vertices)]
dfs_parenteses = ""

def visitaDFS(vertice_analisado, grafo):
  global tempo
  global dfs_parenteses
  global finalizacoes
  tempo += 1
  vetor_entradas[vertice_analisado] = tempo
  dfs_parenteses += f'({vertice_analisado} '
  for vertice in grafo[vertice_analisado]:
    if vetor_entradas[vertice] == -1:
      visitaDFS(vertice, grafo)
  tempo += 1
  if (len(finalizacoes) > 0): finalizacoes[vertice_analisado] = -1
  vetor_saidas[vertice_analisado] = tempo
  dfs_parenteses += f'{vertice_analisado}) '

# Inicializa o DFS para o grafo original
for ordem in range(quantidade_vertices):
  if vetor_entradas[ordem] == -1:
    visitaDFS(ordem, vetor_conexoes)

# Inicializa o DFS para o grafo transposto
tempo = 0
finalizacoes = vetor_saidas
dfs_parenteses = ""
vetor_entradas = [-1 for _ in range(quantidade_vertices)]
vetor_saidas = [-1 for _ in range(quantidade_vertices)]

while not all(item == -1 for item in finalizacoes):
  maior_valor = max(finalizacoes)
  print(maior_valor)
  indice_maior_valor = finalizacoes.index(maior_valor)
  if finalizacoes[indice_maior_valor] != -1:
    visitaDFS(indice_maior_valor, grafo_transposto)
    finalizacoes[indice_maior_valor] = -1
    for vertice in grafo_transposto[indice_maior_valor]:
      finalizacoes[vertice] = -1

print(dfs_parenteses)