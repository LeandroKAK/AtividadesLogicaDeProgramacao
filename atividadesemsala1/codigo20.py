x, y = map(float, input("Insira os valores de (x,y) retire os () : ").split(','))

if x == 0 and y == 0:
    print("Sobre a origem")
elif x == 0: 
    print("Sobre o Eixo Y")
elif y == 0:
    print("Sobre o Eixo X")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")


