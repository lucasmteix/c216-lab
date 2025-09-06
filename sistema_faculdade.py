from collections import Counter

alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    curso = input("Digite o curso do aluno: ")
    alunos.append({"nome": nome, "email": email, "curso": curso,
                   "matricula": nova_matricula(curso)})
    print(f"Aluno {nome} cadastrado com sucesso!")

def nova_matricula(curso):
    numero_matricula = Counter(a["curso"] for a in alunos) + 1
    return curso + str(numero_matricula)

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, E-mail: {aluno['email']}, Sala: {aluno['sala_de_atendimento']}")

def atualizar_aluno():
    nome = input("Digite o nome do aluno a ser atualizado: ")
    for aluno in alunos:
        if aluno["nome"] == nome:
            aluno["email"] = input("Digite o novo e-mail: ")
            aluno["sala_de_atendimento"] = input("Digite a nova sala de atendimento: ")
            print("aluno atualizado com sucesso!")
            return
    print("aluno não encontrado.")

def remover_aluno():
    nome = input("Digite o nome do aluno a ser removido: ")
    for aluno in alunos:
        if aluno["nome"] == nome:
            alunos.remove(aluno)
            print("aluno removido com sucesso!")
            return
    print("aluno não encontrado.")

def main():
    while True:
        print("\nMenu de Opções:")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Atualizar aluno")
        print("4. Remover aluno")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            atualizar_aluno()
        elif opcao == '4':
            remover_aluno()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()