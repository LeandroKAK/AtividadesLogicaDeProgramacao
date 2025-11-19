valor = float(input("Insira o valor inicial: "))
notas = [100,50,20,10,5,2,1]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    quantidade = valor//nota
    valor = valor%nota

    print(f"{int(quantidade)} notas de R$ {float(nota):.2f}")

print("MOEDAS:")
for moeda in moedas:
    quantidade = valor//moeda
    valor = valor%moeda

    print(f"{int(quantidade)} notas de R$ {float(moeda):.2f}")
