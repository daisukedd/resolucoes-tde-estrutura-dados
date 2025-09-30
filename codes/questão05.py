# Matriz fornecida
matriz = [
    [8, 0, 7],
    [4, 5, 6],
    [3, 10, 2]
]

n = len(matriz)

# Soma de referência (primeira linha)
soma_referencia = sum(matriz[0])

# Verifica linhas
linhas_ok = all(sum(linha) == soma_referencia for linha in matriz)

# Verifica colunas
colunas_ok = all(sum(matriz[i][j] for i in range(n)) == soma_referencia for j in range(n))

# Verifica diagonais
diag_principal = sum(matriz[i][i] for i in range(n))
diag_secundaria = sum(matriz[i][n-1-i] for i in range(n))
diagonais_ok = (diag_principal == soma_referencia and diag_secundaria == soma_referencia)

# Resultado
if linhas_ok and colunas_ok and diagonais_ok:
    print("A matriz É um quadrado mágico.")
else:
    print("A matriz NÃO é um quadrado mágico.")
