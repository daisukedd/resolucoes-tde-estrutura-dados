from random import sample

def gerar_cartela():
    numeros = sample(range(100), 25)

    cartela = []
    for i in range(5):
        linha = numeros[i * 5: (i + 1) * 5]
        cartela.append(linha)

    return cartela

def mostar_cartela(cartela):
    print("===== CARTELA DE BINGO =====")
    for linha in cartela:
        for num in linha:
            print(f"{num:02d}", end=" ")
        print()
    print("============================")

cartela = gerar_cartela()
mostar_cartela(cartela)
