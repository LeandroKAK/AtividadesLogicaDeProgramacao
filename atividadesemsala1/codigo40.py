import random
matriz = [[random.randint(1, 10) for j in range(12)] for i in range(12)]
n = int(input('Insira a linha escolhida (1 - 12): ')) - 1
operacao = input('Insira a operação (S/M): ')
if operacao.upper() == 'S':
    resultado = sum(matriz[i][n] for i in range(12))
elif operacao.upper() == 'M':
    resultado = sum(matriz[i][n] for i in range(12)) /12

print(f'Resultado: {resultado}')