n = int(input('Insira o número de testes a ser realizado: '))

# declaração do vetor de resultados
results = []

for i in range(n):
    a, b, c = map(float,input('Insira os 3 valores reais divididos por espaço: ').split())
    media = (a*2 + b*3 + c*5)/10
    results.append(round(media, 1))

print(*results, sep="\n")