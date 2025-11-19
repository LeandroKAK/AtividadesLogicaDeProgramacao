x = 1
while x != 0:
    x = int(input('Insira um valor (Encerra caso 0)'))
    if x % 2 != 0:
        x += 1
    soma = x + (x+2) + (x+4) + (x+6) + (x+8)
    print(soma)