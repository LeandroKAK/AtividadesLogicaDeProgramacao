c1 = str(input("Insira o filo: "))
c2 = str(input("Insira a classe: "))
c3 = str(input("Insira o t: "))

tree = {
    "vertebrado": {
        "ave": {
            "carnivoro": ["aguia"],
            "onivoro": ["pomba"]
        },
        "mamifero": {
            "onivoro": ["homem"],
            "herbivoro": ["vaca"]
        }
    },
    "invertebrado": {
        "inseto": {
            "hematofago": ["pulga"],
            "herbivoro": ["lagarta"]
        },
        "anelideo": {
            "hematofago": ["sanguessuga"],
            "onivoro": ["minhoca"]
        }
    }
}

print(f"Resultado: {tree[c1][c2][c3]}")

# result = tree
# caminho = (c1, c2, c3)
# for etapa in caminho:
#     if isinstance(result, dict) and etapa in result:
#         result = result[etapa]
#     else:
#         result = "Entrada inválida"
#         break

# print(f"Resultado: {result[0] if isinstance(result, list) else result}")