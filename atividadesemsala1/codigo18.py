produtos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

codigo, quantidade = map(int, input("Insira respectivamente o codigo de produto e sua quantidade: ").split())
pagar = produtos[codigo]*quantidade
print(f"Total: R$ {pagar:.2f}")