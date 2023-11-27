def coletar_index(conjunto_disjunto, conjunto_procurado):
    for i, conjunto in enumerate(conjunto_disjunto):
            if conjunto_procurado in conjunto:
                return i

total_operacoes = int(input())
conjunto_disjunto = []

for n in range(total_operacoes):
    operacao = list(tmp for tmp in input().split(" "))

    if (operacao[0] == 'M'):
        conjunto_disjunto.append([operacao[1]])
        print(conjunto_disjunto)

    elif (operacao[0] == 'F'):
        indice = coletar_index(conjunto_disjunto, operacao[1])
        print(f'{indice} {conjunto_disjunto}')

    elif (operacao[0] == 'U'):
        indice_adicionar = coletar_index(conjunto_disjunto, operacao[1])
        indice_remover = coletar_index(conjunto_disjunto, operacao[2])
        conjunto_disjunto[indice_adicionar].append(operacao[2])
        conjunto_disjunto[indice_remover].remove(operacao[2])
        print(conjunto_disjunto)