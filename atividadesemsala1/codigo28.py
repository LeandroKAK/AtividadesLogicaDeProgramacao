n = int(input('Insira o número de testes realizados: '))
tCoelhos = 0
tRatos = 0
tSapos = 0
for i in range(n):
    q, select = input('Insira o numero de cobaias seguido do tipo (C/R/S): ').split()
    q = int(q)
    if select == 'C':
        tCoelhos += q
    elif select == 'R':
        tRatos += q
    elif select == 'S':
        tSapos += q
    else:
        print('Erro na seleção de tipo')
        break

total = tCoelhos + tRatos + tSapos
pCoelhos = round(tCoelhos/total * 100, 2)
pRatos = round(tRatos/total * 100, 2)
pSapos = round(tSapos/total * 100, 2)

print(f"""  Total: {total} cobaias
            Total de coelhos: {tCoelhos}
            Total de ratos: {tRatos}
            Total de sapos: {tSapos}
            Percentual de coelhos: {pCoelhos}%
            Percentual de ratos: {pRatos}%
            Percentual de sapos: {pSapos}%     """)