distanciatotal = float(input("Insira a distancia percorrida em Km: "))
combustivelgasto = float(input("Insira o combustivel gasto em litros: "))

consumomedio = distanciatotal / combustivelgasto

print(f"{consumomedio:.3f} km/l")