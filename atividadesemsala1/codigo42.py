import random
matriz = [[random.randint(1, 10) for j in range(12)] for i in range(12)]
resultado, soma = 0, 0
operacao = input('Insira a operação (S/M): ')
if operacao.upper() == 'S':
    for i in range(12):
        for j in range(12):
            if i > j:
                resultado += matriz[i][j]
elif operacao.upper() == 'M':
    for i in range(12):
        for j in range(12):
            if i > j:
                soma += matriz[i][j]
    resultado = soma/66
    
print(f'Resultado: {resultado}')