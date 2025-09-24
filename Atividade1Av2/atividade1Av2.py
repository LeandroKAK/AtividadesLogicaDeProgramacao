# Declaração da variável pares
pares = 0

# range para leitura dos 5 valores e verificar par
for i in range(5):
    a = int(input(f"Insira o valor {i+1}: "))
    if (a%2) == 0 :
        pares += 1

# Saída
print(f"{pares} valores pares")
