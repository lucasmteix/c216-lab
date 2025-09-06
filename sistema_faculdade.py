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
    contagem = sum(1 for a in alunos if a["curso"] == curso)
    return curso + str(contagem + 1)

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, E-mail: {aluno['email']}, Matrícula: {aluno['matricula']}")

def atualizar_aluno():
    nome = input("Digite o nome do aluno a ser atualizado: ")
    for aluno in alunos:
        if aluno["nome"] == nome:
            aluno["email"] = input("Digite o novo e-mail: ")
            curso = input("Digite o novo curso: ")
            aluno["matricula"] = nova_matricula(curso)
            aluno["curso"] = curso # curso eh atualizado depois de matricula para nao causar
            # erro de contagem no numero da nova matricula
            print("Aluno atualizado com sucesso!")
            return
    print("Aluno não encontrado.")

def remover_aluno():
    nome = input("Digite o nome do aluno a ser removido: ")
    for aluno in alunos:
        if aluno["nome"] == nome:
            alunos.remove(aluno)
            print("Aluno removido com sucesso!")
            return
    print("Aluno não encontrado.")

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