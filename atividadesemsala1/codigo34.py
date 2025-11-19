codigo, alcool, gasolina, diesel = 0, 0, 0, 0
while codigo != 4:
    codigo = int(input('Insira o codigo do combustivel 1.Álcool 2.Gasolino 3.Diesel (4 finaliza o programa): '))
    print(codigo)
    if codigo == 1:
        alcool += 1
    elif codigo == 2:
        gasolina += 1
    elif codigo == 3:
        diesel += 1

print(f'MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}')