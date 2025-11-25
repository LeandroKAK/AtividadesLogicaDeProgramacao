x = int(input('insira o valor 1: '))
y = int(input('insira o valor 2: '))

soma = 0

while x <= y:
    if x % 13 != 0:
        soma += x
    x += 1

print(f'Resultado da soma: {soma}')