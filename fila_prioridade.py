tamanho_fila, quantidade_operacoes = (int(tmp) for tmp in input().split(" "))
fila_prioridade = [0 for _ in range(tamanho_fila)]

fila = list(int(tmp) for tmp in input().split(" "))

def achar_valor_minimo(fila, fila_prioridade):
    valor_minimo = float('inf')

    for i in range(len(fila_prioridade)):
        if fila_prioridade[i] == 1:
            valor_minimo = min(valor_minimo, fila[i])

    return valor_minimo

for i in range(quantidade_operacoes):
    operacao = list(tmp for tmp in input().split(" "))

    if (operacao[0] == 'I'):
        index = int(operacao[1])
        fila_prioridade[index] = 1
        print(fila_prioridade)
    
    elif (operacao[0] == 'E' or operacao[0] == 'M'):
        valor_minimo = achar_valor_minimo(fila, fila_prioridade)
        indice_minimo = fila.index(valor_minimo)
        if (operacao[0] == 'E'):
            fila_prioridade[indice_minimo] = 0
        print(f'{indice_minimo} {valor_minimo} {fila_prioridade}')

    elif (operacao[0] == 'B'):
        valor = int(operacao[1])
        resultado = 1 if valor in fila else 0
        print(f'{resultado} {fila_prioridade}')

    elif (operacao[0] == 'V'):
        resultado = all(elemento == 0 for elemento in fila_prioridade)
        print(f'{resultado} {fila_prioridade}')