a, b, c = map(float, input("Digite os valores de A, B e C respectivamente separados por espaço: ").split())

triangulo = (a*c)/2
circulo = 3.14159 * (c**2)
trapezio = ((a+b) * c)/2
quadrado = b**2
retangulo = a*b

print(f"TRIANGULO: {triangulo:.3}\nCIRCULO: {circulo}\n TRAPEZIO:{trapezio}\n QUADRADO: {quadrado}\n RETANGULO:{retangulo}")