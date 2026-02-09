professor = {}
turma = []
nome_turma = ""


def cabecalho():
    print("==============================")
    print(f"Professor: {professor['nome']}")
    print(f"Disciplina: {professor['disciplina']}")
    print(f"Turma: {nome_turma}")
    print("==============================")


def criar_professor():
    global nome_turma
    print(" === Criar Professor e Turma ===")
    professor["nome"] = input("Nome do professor: ")
    professor["disciplina"] = input("Disciplina: ")
    nome_turma = input("Turma: ")
    print("Professor e turma criados com sucesso")


def adicionar_aluno():
    while True:
        print("=== Adicionar Aluno ===")
        nome = input("Nome do aluno: ")
        numero = input("Número do aluno: ")

        aluno = {
            "nome": nome,
            "numero": numero,
            "faltas": 0,
            "faltas_material": 0,
            "ocorrencias": []
        }

        turma.append(aluno)
        print("Aluno adicionado com sucesso")

        continuar = input("Deseja adicionar outro aluno (s/n): ").lower()
        if continuar != "s":
            break


def listar_alunos():
    print("=== Lista de Alunos ===")
    if len(turma) == 0:                                                 
        print("Não existem alunos na turma.\n")
        return

    for aluno in turma:
        print(
            f"{aluno['numero']} - {aluno['nome']} | "
            f"Faltas: {aluno['faltas']} | "
            f"Falta material: {aluno['faltas_material']}"
        )
    print()


def marcar_falta():
    numero = input("Número do aluno: ")
    for aluno in turma:
        if aluno["numero"] == numero:
            aluno["faltas"] += 1
            print("Falta marcada com sucesso!")
            return
    print("Aluno não encontrado.")


def marcar_falta_material():
    numero = input("Número do aluno: ")
    for aluno in turma:
        if aluno["numero"] == numero:
            aluno["faltas_material"] += 1
            print("Falta de material registada")
            return
    print("Aluno não encontrado.")


def registar_ocorrencia():
    numero = input("Número do aluno: ")
    for aluno in turma:
        if aluno["numero"] == numero:
            ocorrencia = input("Descrição da ocorrência: ")
            aluno["ocorrencias"].append(ocorrencia)
            print("Ocorrência registada!")
            return
    print("Aluno não encontrado.")


def consultar_aluno():
    numero = input("Número do aluno: ")
    for aluno in turma:
        if aluno["numero"] == numero:
            print("=== Dados do Aluno ===")
            print("Nome:", aluno["nome"])
            print("Número:", aluno["numero"])
            print("Faltas:", aluno["faltas"])
            print("Faltas de material:", aluno["faltas_material"])
            print("Ocorrências:")
            if len(aluno["ocorrencias"]) == 0:
                print("  Nenhuma ocorrência.")
            else:
                for o in aluno["ocorrencias"]:
                    print(" -", o)
            print()
            return
        print("Aluno não encontrado: ")


def remover_alunos():
    numero = input("Número do aluno: ")
    for aluno in turma:
        if aluno["numero"] == numero:
            turma.remove(aluno)
            print(f"Aluno {aluno['nome']} removido com sucesso!")
            return
    print("Aluno não encontrado.")


def menu():
    while True:

        # Se ainda não existir professor criado
        if not professor:
            print("=== Gestor de Turma ===")
            print("1 - Criar professor, disciplina e turma")
            print("0 - Sair")

            opcao = input("Opção: ")

            if opcao == "1":
                criar_professor()
            elif opcao == "0":
                print("A sair do sistema...")
                break
            else:
                print("Opção inválida.")

        # Depois de criado o professor
        else:
            cabecalho()
            print("1 - Adicionar aluno")
            print("2 - Listar alunos")
            print("3 - Marcar falta")
            print("4 - Marcar falta de material")
            print("5 - Registar ocorrência disciplinar")
            print("6 - Consultar aluno")
            print("7 - remover alunos")
            print("0 - Sair")

            opcao = input("Opção: ")

            if opcao == "1":
                adicionar_aluno()
            elif opcao == "2":
                listar_alunos()
            elif opcao == "3":
                marcar_falta()
            elif opcao == "4":
                marcar_falta_material()
            elif opcao == "5":
                registar_ocorrencia()
            elif opcao == "6":
                consultar_aluno()
            elif opcao == "7":
                remover_alunos()
            elif opcao == "0":
                print("A sair do sistema...")
                break
            else:
                print("Opção inválida.")


menu()
