import math

x1, y1 = map(float,input("Insira p1 (dessa forma 'x1 y1')").split())
x2, y2 = map(float,input("Insira p2 (dessa forma 'x2 y2')").split())

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"A distância entre eles será {distancia:.4f}")