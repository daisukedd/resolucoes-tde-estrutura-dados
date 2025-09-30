valor_a = 3 
valor_b = 3
vetor = []
cont = 0
ed_valores = [[0] * valor_b for _ in range(valor_a)]
matriz_antes = [row[:] for row in ed_valores]
print("output:")
for linha in ed_valores:
    print(linha)

for m in range(valor_a):
    for n in range(len(ed_valores[m])):
        ed_valores[m][n] = int(input("Digite um valor: "))
        if ed_valores[m][n] > 4:
            vetor.append(ed_valores[m][n])
            cont += 1
