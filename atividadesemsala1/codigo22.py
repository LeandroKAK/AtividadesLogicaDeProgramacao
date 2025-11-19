a,b = map(int,input("Insira os valores A e B: ").split())

if a%b == 0 or b%a == 0:
    print("Sao Multiplos")
else:
    print("Nao Sao Multiplos")