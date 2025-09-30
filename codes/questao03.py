tam = 8
vetor = [0] * tam  # inicialização do vetor

# preenchendo o vetor
for i in range(tam):
    vetor[i] = int(input(f"Digite o valor da posição {i}: "))

# recebendo as posições
x = int(input(f"Digite a posição X (0 a {tam-1}): "))
y = int(input(f"Digite a posição Y (0 a {tam-1}): "))

# validation
if 0 <= x < tam and 0 <= y < tam:
    soma = vetor[x] + vetor[y]
    print(f"A soma dos valores nas posições {x} e {y} é: {soma}")
else:
    print("Posições inválidas! Digite valores entre 0 e 7.")
