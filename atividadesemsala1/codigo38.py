n = int(input('Insira o numero de valores no vetor: '))
vetor = []
for i in range(n):
    vetor.append(float(input(f'Insira o valor {i} do vetor: ')))
    if i == 0:
        menorValor = vetor[i]
        posicao = 0
    if vetor[i] < menorValor:
        menorValor = vetor[i]
        posicao = i
    
print(f'Menor valor: {menorValor}\n Posicao: {posicao}')