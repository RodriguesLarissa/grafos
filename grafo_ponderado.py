quantidade_vertices, quantidade_arcos = (int(tmp) for tmp in input().split(" "))
vetor_conexoes = [{} for _ in range(quantidade_vertices)]

for i in range(quantidade_arcos):
    vertice_origem, vertice_destino, peso = (int(tmp) for tmp in input().split(" "))
    vetor_conexoes[vertice_origem][vertice_destino] = peso

for index, vertice in enumerate(vetor_conexoes):
    conexao_str = ' '.join(f'{destino}({peso})' for destino, peso in vertice.items())
    print(f'{index}: {conexao_str}')