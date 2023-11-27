quantidade_vertices, quantidade_arcos = (int(tmp) for tmp in input().split(" "))
vetor_conexoes = [{} for _ in range(quantidade_vertices)]
grafo = [[[float('inf')] * quantidade_vertices for _ in range(quantidade_vertices)] for _ in range(quantidade_vertices+1)]
vizinhos = [[-1] * quantidade_vertices for _ in range(quantidade_vertices)]

for i in range(quantidade_arcos):
  vertice_origem, vertice_destino, peso = (int(tmp) for tmp in input().split(" "))
  vetor_conexoes[vertice_origem][vertice_destino] = peso

for vertice in range(quantidade_vertices):
  grafo[0][vertice][vertice] = 0

  for subvertice in vetor_conexoes[vertice]:
    grafo[0][vertice][subvertice] = vetor_conexoes[vertice][subvertice]
    vizinhos[vertice][subvertice] = vertice

for k in range(0, quantidade_vertices):
  for i in range(0, quantidade_vertices):
    for j in range(0, quantidade_vertices):
        grafo[k+1][i][j] = min(grafo[k][i][j], grafo[k][i][k] + grafo[k][k][j])
        if grafo[k][i][j] > grafo[k][i][k] + grafo[k][k][j]:
            vizinhos[i][j] = vizinhos[k][j]

print(grafo[quantidade_vertices])
print(vizinhos)