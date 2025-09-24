# Entrada
n = int(input("Insira a quantidade de numeros a serem inseridos: "))

# Declaração das variáveis
dentro = 0
fora = 0

for i in range(n):
    x = int(input(f"Insira o valor {i+1}: "))
    if x >= 10 and x <= 20:
        dentro += 1
    else:
        fora += 1

print(f"{dentro} in\n{fora} out")
        