# Declaração do preço base

preco = 20

# Entradas requisitadas

idade = int(input("Insira sua idade "))
if idade < 0:
    print("Erro, idade inválida")
    exit()
if idade > 120:
    print("Erro, idade inválida")
    exit()
estudante = str(input("É estudante? (S/N) "))

# Verificações e Saídas

if idade < 12:
    preco = preco/2
    print("meia entrada para criança")
if estudante == 'S':
    preco = preco/2
    print("meia entrada para estudante")
if idade > 60:
    preco = preco/2
    print("meia entrada para idoso")
else:
    print(f"Valor do ingresso: R${preco}")

