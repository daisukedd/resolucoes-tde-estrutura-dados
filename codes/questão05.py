matriz = [
    [8, 0, 7],
    [4, 5, 6],
    [3, 10, 2]
]

n = len(matriz)
soma_referencia = sum(matriz[0])

def soma_linha(linha):
    return sum(linha)

def soma_coluna(j):
    return sum(matriz[i][j] for i in range(n))

linhas_ok = all(soma_linha(linha) == soma_referencia for linha in matriz)
colunas_ok = all(soma_coluna(j) == soma_referencia for j in range(n))
diag_principal = sum(matriz[i][i] for i in range(n))
diag_secundaria = sum(matriz[i][n-1-i] for i in range(n))
diagonais_ok = diag_principal == soma_referencia and diag_secundaria == soma_referencia

if linhas_ok and colunas_ok and diagonais_ok:
    print("A matriz é um quadrado mágico.")
else:
    print("A matriz não é um quadrado mágico.")
