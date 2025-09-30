def input_answer(question_num):
    answer = input(f"Questão {question_num} (a, b, c, d ou e): ").lower()
    while answer not in ['a', 'b', 'c', 'd', 'e']:
        answer = input("Opção inválida! Digite (a, b, c, d ou e): ").lower()
    return answer

def register_answer_key():
    print("\n=== Cadastro do Gabarito ===")
    return [input_answer(i + 1) for i in range(10)]

def register_students(answer_key):
    students = []
    print("\n=== Cadastro dos Alunos ===")
    for i in range(3):
        print(f"\nAluno {i + 1}:")
        student_id = int(input("Matrícula: "))
        answers = [input_answer(j + 1) for j in range(10)]
        score = sum(1 for k in range(10) if answers[k] == answer_key[k])
        percentage = (score / 10) * 100
        status = "APROVADO" if score >= 7 else "REPROVADO"
        students.append({
            "id": student_id,
            "answers": answers,
            "score": score,
            "percentage": percentage,
            "status": status
        })
    return students

def print_results(students):
    print("\n=== RESULTADOS ===")
    for student in students:
        print(f"\nMatrícula: {student['id']}")
        print("Respostas:", " | ".join(student['answers']))
        print(f"Nota: {student['score']}/10")
        print(f"Percentual: {student['percentage']}%")
        print(f"Situação: {student['status']}")
        print("-" * 40)

def main():
    answer_key = []
    students = []

    while True:
        print("\n=== Sistema de Correção de Provas ===")
        print("1 – Cadastrar gabarito")
        print("2 – Cadastrar alunos")
        print("3 – Mostrar resultados")
        print("0 – Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            answer_key = register_answer_key()
        elif choice == "2":
            if not answer_key:
                print("Cadastre o gabarito primeiro!")
            else:
                students = register_students(answer_key)
        elif choice == "3":
            if not students:
                print("Cadastre os alunos primeiro!")
            else:
                print_results(students)
        elif choice == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
