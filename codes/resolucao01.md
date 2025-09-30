# Resolução da Questão 01 do TDE de Estrutura de Dados

## Contexto

O código fornecido implementa uma matriz **3x3** em Python, permitindo a entrada manual de valores pelo usuário.
Adicionalmente, um vetor armazena apenas os valores da matriz que são **maiores que 4**, registrando a quantidade de elementos filtrados por meio de um contador (`cont`).

---

## Estrutura do Código

```python
valor_a = 3 
valor_b = 3
vetor = []
cont = 0

# Inicialização da matriz 3x3 preenchida com zeros
ed_valores = [[0] * valor_b for _ in range(valor_a)]

# Entrada de dados e filtragem
for m in range(valor_a):
    for n in range(len(ed_valores[m])):
        ed_valores[m][n] = int(input("Digite um valor: "))
        if ed_valores[m][n] > 4:
            vetor.append(ed_valores[m][n])
            cont += 1
```

---

## Saída Esperada (Exemplo de Execução)

### Entrada do usuário:

```
4, 6, 7, 1, 10, 8, 13, 14, 15
```

### Estrutura da Matriz:

```
[4,  6,  7]
[1, 10,  8]
[13, 14, 15]
```

### Estrutura do Vetor:

```
[6, 7, 10, 8, 13, 14, 15]
```

---

## Avaliação das Alternativas

| Item  | Análise                                                                                                                               | Resultado    |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **a** | O código define **uma matriz (`ed_valores`)** e **um vetor (`vetor`)**. Não há duas matrizes.                                         | ❌ Falsa      |
| **b** | A validação `> 4` ocorre **após** a atribuição do valor na matriz, e não no momento da entrada.                                       | ❌ Falsa      |
| **c** | A variável `cont` controla a posição e quantidade de elementos adicionados ao vetor.                                                  | ✅ Verdadeira |
| **d** | `cont` **não indica o tamanho fixo** do vetor, apenas quantos valores foram adicionados. O vetor cresce dinamicamente com `append()`. | ❌ Falsa      |
| **e** | O valor **14** está na matriz em `[2][1]`. No vetor `[6, 7, 10, 8, 13, 14, 15]`, encontra-se na posição `[5]`.                        | ✅ Verdadeira |

---

## Conclusão

As alternativas corretas são:

* ✅ **(c) e (e)**
* ❌ **(a), (b) e (d)**

---

## Critérios Técnicos Utilizados

1. **Modelagem de dados** – matriz representada por lista de listas e vetor como lista linear.
2. **Estrutura de controle** – laços `for` duplos para percorrer linhas e colunas.
3. **Validação condicional** – uso de `if` para filtrar valores maiores que `4`.
4. **Contador (`cont`)** – atua como índice incremental e como medidor de elementos válidos no vetor.
5. **Documentação** – explicação clara do fluxo e uso de exemplos reais de execução.

---

## Referências

* [Python Official Docs – Lists](https://docs.python.org/3/tutorial/datastructures.html)
* [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

---