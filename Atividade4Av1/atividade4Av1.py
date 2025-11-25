n = int(input('Insira um inteiro positivo: '))
resultado = n

while n > 1:
    n -= 1
    resultado *= n

print(f'Resultado do fatorial: {resultado}')