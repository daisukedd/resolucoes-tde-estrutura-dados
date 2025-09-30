tam = 8
vetor = [int] * tam

for i in range(len(vetor)):
    vetor[i] = int(input(f"Digite o valor da posição {i}: "))

x = int(input("Digite a posição X (0 a 7): "))
y = int(input("Digite a posição Y (0 a 7): "))

if 0 <= x < 8 and 0 <= y < 8:
    soma = vetor[x] + vetor[y]
    print(f"A soma dos valores nas posições {x} e {y} é: {soma}")
else:
    print("Posições inválidas! Digite valores entre 0 e 7.")
