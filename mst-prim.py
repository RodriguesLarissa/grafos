def extrair_minimo(vetor_distancias, vetor_concluidas):
    valores_filtrados = [float('inf') if valor == 1 else elemento for valor, elemento in zip(vetor_concluidas, vetor_distancias)]
    return valores_filtrados.index(min(valores_filtrados))

quantidade_vertices, quantidade_arcos, chave = (int(tmp) for tmp in input().split(" "))
vetor_conexoes = [{} for _ in range(quantidade_vertices)]
distancias = [float('inf')] * quantidade_vertices
pais = [-1] * quantidade_vertices
concluidos = [-1] * quantidade_vertices

for i in range(quantidade_arcos):
  vertice_origem, vertice_destino, peso = (int(tmp) for tmp in input().split(" "))
  vetor_conexoes[vertice_origem][vertice_destino] = peso

distancias[chave] = 0
while any(item == -1 for item in concluidos):
    chave = extrair_minimo(distancias, concluidos)
    for vizinho in vetor_conexoes[chave]:
        if distancias[vizinho] > vetor_conexoes[chave][vizinho] and concluidos[vizinho] == -1:
            distancias[vizinho] = vetor_conexoes[chave][vizinho]
            pais[vizinho] = chave
    concluidos[chave] = 1

print(distancias)
print(pais)