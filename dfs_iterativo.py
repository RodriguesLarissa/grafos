# DFS por iteração
tempo = 0
pilha = []
quantidade_vertices, quantidade_arcos = (int(tmp) for tmp in input().split(" "))
vetor_entradas = [-1 for _ in range(quantidade_vertices)]
vetor_saidas = [-1 for _ in range(quantidade_vertices)]
vetor_conexoes = [[] for _ in range(quantidade_vertices)]

for i in range(quantidade_arcos):
  vertice_origem, vertice_destino = (int(tmp) for tmp in input().split(" "))
  vetor_conexoes[vertice_origem].append(vertice_destino)

# Inicializa o DFS
for ordem in range(quantidade_vertices):
  if vetor_entradas[ordem] == -1:
    pilha.append(ordem)
    while len(pilha) != 0:
      primeiro_vertice_nao_visitado = None
      vertice_analisado = pilha[-1];
      if vetor_entradas[vertice_analisado] == -1:
        tempo += 1
        vetor_entradas[vertice_analisado] = tempo

      for vertice_vizinho in vetor_conexoes[vertice_analisado]:
        if vetor_entradas[vertice_vizinho] == -1 and vertice_vizinho not in pilha:
          primeiro_vertice_nao_visitado = vertice_vizinho
          break

      if primeiro_vertice_nao_visitado is not None:
        pilha.append(primeiro_vertice_nao_visitado)
      else:
          tempo += 1
          vetor_saidas[vertice_analisado] = tempo
          pilha.pop(-1)

print(vetor_entradas)
print(vetor_saidas)