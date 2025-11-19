n = int(input("Insira a duração em segundos: "))

horas = n // 3600
n = n%3600

minutos = n //60
n = n%60

segundos = n

print(f"{horas}:{minutos}:{segundos}")