def ordenar_pilha(pilha):
    pilha_aux = []  # pilha auxiliar

    while pilha:  # enquanto a pilha original não estiver vazia
        tmp = pilha.pop()  # tira o topo da pilha original

        # Move os elementos maiores de pilha_aux de volta para pilha
        while pilha_aux and pilha_aux[-1] > tmp:
            pilha.append(pilha_aux.pop())

        # Coloca o elemento na pilha auxiliar
        pilha_aux.append(tmp)

    # Move os elementos de volta para pilha (ordenada)
    while pilha_aux:
        pilha.append(pilha_aux.pop())

    return pilha

pilha = [5, 30, 25, 10, 15, 20]  
print("Pilha original:", pilha)

ordenada = ordenar_pilha(pilha)
print("Pilha ordenada (crescente):", ordenada)
