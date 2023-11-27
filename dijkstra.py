def extrair_minimo(vetor_distancias, vetor_concluidas):
    valores_filtrados = [float('inf') if valor == 1 else elemento for valor, elemento in zip(vetor_concluidas, vetor_distancias)]
    return valores_filtrados.index(min(valores_filtrados))

quantidade_vertices, quantidade_arcos, vertice_inicial = (int(tmp) for tmp in input().split(" "))
vetor_conexoes = [{} for _ in range(quantidade_vertices)]
vetor_distancias = [0] * quantidade_vertices
vetor_concluidos = [0] * quantidade_vertices
vetor_caminho = [-1] * quantidade_vertices

for i in range(quantidade_arcos):
    vertice_origem, vertice_destino, peso = (int(tmp) for tmp in input().split(" "))
    vetor_conexoes[vertice_origem][vertice_destino] = peso

for vertice in range(quantidade_vertices):
    vetor_distancias[vertice] = float('inf')

vetor_distancias[vertice_inicial] = 0

while not all(elemento == 1 for elemento in vetor_concluidos):
    vertice_minimo = extrair_minimo(vetor_distancias, vetor_concluidos)
    for vertice in vetor_conexoes[vertice_minimo]:
        if vetor_distancias[vertice_minimo] + vetor_conexoes[vertice_minimo][vertice] < vetor_distancias[vertice]:
            vetor_distancias[vertice] = vetor_distancias[vertice_minimo] + vetor_conexoes[vertice_minimo][vertice]
            vetor_caminho[vertice] = vertice_minimo
        vetor_concluidos[vertice_minimo] = 1

print(vetor_distancias)
print(vetor_caminho)