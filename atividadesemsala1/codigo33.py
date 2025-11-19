while True:
    nota1 = float(input(f"Insira a nota 1: "))
    if nota1 < 0 or nota1 > 10:
        print('Nota inválida')
    else:
        break

while True:
    nota2 = float(input(f"Insira a nota 2: "))
    if nota2 < 0 or nota2 > 10:
        print('Nota inválida')
    else:
        break

print('média = ', round((nota1 + nota2)/2, 2))