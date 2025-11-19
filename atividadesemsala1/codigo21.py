v1,v2,v3 = map(int,input("Insira 3 valores inteiros: ").split())

if v1 > v2:
    maior = v1
    menor = v2
else:
    maior = v2
    menor = v1

if v3 > maior:
    print(f"{menor}\n{maior}\n{v3}")
elif v3 > menor: 
    print(f"{menor}\n{v3}\n{maior}")
else:
    print(f"{v3}\n{menor}\n{maior}")

print(f"\n{v1}\n{v2}\n{v3}")