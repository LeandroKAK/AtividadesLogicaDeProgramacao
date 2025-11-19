valores = map(float, input("Insira 6 valores diferentes: ").split())

positivos = []

positivosQ = 0

for valor in valores:
    if valor >= 0:
        positivosQ += 1
        positivos.append(valor)

media = sum(positivos) / len(positivos)

print(f"{positivosQ} valores positivos")
print(f"A média dos valores será {media:.1f}")