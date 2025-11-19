import sys

n1,n2,n3 = map(float,input("Insira 3 valores: ").split())

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

if n3 > maior:
    a, b, c = (n3, maior, menor)
elif n3 > menor: 
    a, b, c = (maior, n3, menor)
else:
    a, b, c = (maior, menor, n3)

if a >= (b+c):
    print("NAO FORMA TRIANGULO")
sys.exit()

if a**2 == ((b**2) + (c**2)):
    print("TRIANGULO RETANGULO")
elif a**2 > ((b**2) + (c**2)):
    print("TRIANGULO OBTUSANGULO")
elif a**2 < ((b**2) + (c**2)):
    print("TRIANGULO ACUTANGULO")

if a == b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or a == c or b == c:
    print("TRIANGULO ISOSCELES")    