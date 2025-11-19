# Entrada e declaração da variável tentativas
n = int(input("Adivinhe o número (entre 1 e 10): "))
tentativas = 1

# Tentativa 1
if n < 1:
    print("Palpite Inválido!")  
if n > 10:
    print("Palpite Inválido!")    
if n == 7:
    print(f"Acertou você usou {tentativas} tentativas")
    exit()
if n < 7:
    if n >= 1:
        if n <= 10:
            print("Muito Baixo!")
if n > 7:
    if n >= 1:
        if n <= 10:
            print("Muito Alto!")      
tentativas += 1

# Tentativa 2
n = int(input("Adivinhe o número (entre 1 e 10): "))

if n < 1:
    print("Palpite Inválido!")  
if n > 10:
    print("Palpite Inválido!")    
if n == 7:
    print(f"Acertou você usou {tentativas} tentativas")
    exit()
if n < 7:
    if n >= 1:
        if n <= 10:
            print("Muito Baixo!")
if n > 7:
    if n >= 1:
        if n <= 10:
            print("Muito Alto!")      
tentativas += 1

# Tentativa 3
n = int(input("Adivinhe o número (entre 1 e 10): "))

if n < 1:
    print("Palpite Inválido!")  
if n > 10:
    print("Palpite Inválido!")    
if n == 7:
    print(f"Acertou você usou {tentativas} tentativas")
    exit()
if n < 7:
    if n >= 1:
        if n <= 10:
            print("Muito Baixo!")
if n > 7:
    if n >= 1:
        if n <= 10:
            print("Muito Alto!")      
tentativas += 1