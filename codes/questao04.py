def traduzir(indices_secretos):
    codigo = [' '] + list("abcdefghijklmnopqrstuvwxyz")
    mensagem = ""
    for indice in indices_secretos:
        if 0 <= indice < len(codigo):
            mensagem += codigo[indice]
        else:
            mensagem += "?"
    return mensagem

indices_secretos = [2, 15, 13, 0, 4, 9, 1]
print("Mensagem Decifrada:", traduzir(indices_secretos))
