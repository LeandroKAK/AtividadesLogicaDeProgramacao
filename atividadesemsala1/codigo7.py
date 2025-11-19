numero = int(input("Insira o numero do funcionário: "))
horasdetrabalho = int(input("Insira a quantidade de horas trabalhadas: "))
pagamentoporhora = float(input("Insira o valor ganho por hora: "))

salario = horasdetrabalho * pagamentoporhora

print(f"NUMBER = {numero}")
print(f"SALARY = U$ {salario}")