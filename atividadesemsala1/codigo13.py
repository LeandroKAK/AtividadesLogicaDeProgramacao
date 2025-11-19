valor = int(input("Insira o valor inicial: "))
notas = [100,50,20,10,5,2,1]

for nota in notas:
    quantidade = valor//nota
    valor = valor%nota

    print(f"{quantidade} notas de R$ {float(nota):.2f}")