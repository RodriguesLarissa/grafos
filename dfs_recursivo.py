# DFS por recursão
tempo = 0
vertice_inicial = 0
quantidade_vertices, quantidade_arcos = (int(tmp) for tmp in input().split(" "))
vetor_entradas = [-1 for _ in range(quantidade_vertices)]
vetor_saidas = [-1 for _ in range(quantidade_vertices)]
vetor_conexoes = [[] for _ in range(quantidade_vertices)]

def visitaDFS(vertice_analisado):
  global tempo
  tempo += 1
  vetor_entradas[vertice_analisado] = tempo
  for vertice in vetor_conexoes[vertice_analisado]:
    if vetor_entradas[vertice] == -1:
      visitaDFS(vertice)
  tempo += 1
  vetor_saidas[vertice_analisado] = tempo

for i in range(quantidade_arcos):
  vertice_origem, vertice_destino = (int(tmp) for tmp in input().split(" "))
  vetor_conexoes[vertice_origem].append(vertice_destino)

# Inicializa o DFS
for ordem in range(quantidade_vertices):
  if vetor_entradas[ordem] == -1:
    visitaDFS(ordem)

print(vetor_entradas)
print(vetor_saidas)