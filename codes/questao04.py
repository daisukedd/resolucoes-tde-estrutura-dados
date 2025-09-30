def traduzir(ISecreta):
    codigo = [' ', 'a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    mensagem = ''
    for i in range(len(ISecreta)):
        mensagem += codigo[ISecreta[i]]

    return mensagem

ISecreta = [2, 15, 13, 0, 4, 9, 1]
print("Mensagem decifrada:", traduzir(ISecreta))
