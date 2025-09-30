valor_a = 3
valor_b = 3
vetor = [int] * 9
cont = 0
ed_valores = [0] * valor_a

for l in range(len(ed_valores)):
    ed_valores[l] = [0] * valor_b

for m in range(len(ed_valores)):
    for n in range(len(ed_valores[m])):
        ed_valores[m][n] = int(input("Digite o valor \t"))
        if ed_valores[m][n] > 4:
            vetor[cont] = ed_valores[m][n]
            cont += 1
