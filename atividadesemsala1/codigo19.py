n1, n2, n3, n4 = map(float,input("Insira os valors das 4 provas respectivamente: ").split())

media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10

print(f"Média = {media}")
if media < 5.0:
    print("Aluno Reprovado")
elif media >= 7.0:
    print("Aluno Aprovado")
else:
    print("Aluno em exame")
    exame = float(input("Nota do exame: "))
    media = (media + exame)/2
    if media >= 5:
        print("Aluno Aprovado")
    else:
        print("Aluno reprovado")
    
print(f"Média final = {media:.1f}")