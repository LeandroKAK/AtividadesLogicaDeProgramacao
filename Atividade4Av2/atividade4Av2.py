casos = int(input('Insira a quantidade de testes: '))

while casos > 0:
    n = int(input('Insira o numero teste: '))
    verificadorPrimo = 1

    if n <= 1:
        verificadorPrimo = 0
    count = 2

    while count <= n / 2:
        if n % count == 0:
            verificadorPrimo = 0
            break
        count += 1

    if verificadorPrimo == 1:
        print(f'{n} é primo')
    else:
        print(f'{n} não é primo')
    casos -= 1