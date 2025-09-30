from random import sample

def gerar_cartela():
    numeros = sample(range(100), 25)
    cartela = [numeros[i*5:(i+1)*5] for i in range(5)]
    return cartela

def mostrar_cartela(cartela):
    print("===== CARTELA DE BINGO ===")
    for linha in cartela:
        print("| " + " | ".join(f"{num:02d}" for num in linha) + " |")
        print("+----+----+----+----+----+")

cartela = gerar_cartela()
mostrar_cartela(cartela)
