print("=== Cadastro do Gabarito ===")
gabarito = []
for i in range(10):
    resposta = input(f"Resposta da questão {i + 1} (a, b, c, d ou e): ").lower()
    while resposta not in ['a', 'b', 'c', 'd', 'e']:
        resposta = input("Opção inválida! Digite (a, b, c, d ou e): ").lower()
    gabarito.append(resposta)

print("\n=== Cadastro dos Aluno ===")
alunos = []

for i in range(3):
    print(f"\nAluno {i + 1}:")
    matricula = int(input("Digite a matrícula: "))
    respostas = []
    for j in range(10):
        r = input(f"Resposta do aluno para a questão {j + 1}: ").lower()
        while r not in ['a', 'b', 'c', 'd', 'e']:
            r = input("Opção inválida! Digite (a, b, c, d, ou e): ").lower()
        respostas.append(r)

    nota = 0
    for k in range(10):
        if respostas[k] == gabarito[k]:
            nota += 1

    percentual = (nota / 10) * 100
    status = "APROVADO" if nota >= 7 else "REPROVADO"

    alunos.append({
        "matricula": matricula,
        "respostas": respostas,
        "nota": nota,
        "percentual": percentual,
        "status": status
    })

print("\n=== RESULTADOS ===")
for aluno in alunos:
    print(f"\nMatrícula: {aluno['matricula']}")
    print(f"Respostas: {aluno['respostas']}")
    print(f"Nota: {aluno['nota']}/10")
    print(f"Percentual: {aluno['percentual']}%")
    print(f"Situação: {aluno['status']}")
