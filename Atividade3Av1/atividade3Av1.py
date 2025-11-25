loop = 1

while loop != 2:
    media = 0
    x = 1
    while x < 3:
        nota = float(input(f'Insira a nota {x}: '))
        while nota > 10 or nota < 0:
            print('Nota inválida')
            nota = 0
            x -= 1
        media += nota
        x += 1

    media = media/2

    print(f'Média = {media:.3}')

    loop = 0

    while loop != 1 and loop != 2:
        loop = int(input('Novo cálculo? (1-sim 2-não) '))