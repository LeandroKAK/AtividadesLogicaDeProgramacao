vetor = []
for i in range(10):
    vetor.append(int(input(f'Insira o número {i} para o vetor ')))
    i += 1

for i in range(10):
    if vetor[i] < 1:
        vetor[i] = 1

for i in range(10):
    print(f'X[{i}] = {vetor[i]}')
    i += 1