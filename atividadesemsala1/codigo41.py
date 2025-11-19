matriz = []
n = 1
while n > 0:
    n = int(input('Insira um positivo inteiro (0 encerra o programa): '))
    for i in range(n):
        linha = []
        for j in range(n):
            valor = min(i, j, n - 1 - i, n - 1 - j) + 1
            linha.append(valor)
        matriz.append(linha)
    for linha in matriz:
        print(" ".join(f"{v:3d}" for v in linha))
    print()