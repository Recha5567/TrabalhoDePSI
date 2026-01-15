# Lista para guardar as notas
notas = []

# Função para inserir notas
def inserir_notas():
    while True:
        nota = float(input("Introduz uma nota (0 a 20): "))
        if 0 <= nota <= 20:
            notas.append(nota)
        else:
            print("Nota errada escreve bem!")

        continuar = input("Queres meter mais alguma nota? (sim/não): ")
        if continuar.lower() != 's':
            break

# Função para listar notas
def listar_notas():
    if len(notas) == 0:
        print("Não existem notas registadas.")
    else:
        print("Notas registadas:")
        for n in notas:
            print(n)

# Função para calcular a média
def calcular_media():
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

# Função para atribuir classificação
def classificacao(media):
    if media < 10:
        return "Reprovado"
    elif media < 14:
        return "Suficiente"
    elif media < 18:
        return "Bom"
    else:
        return "Muito Bom"

# Menu principal
def menu():
    while True:
        print("Notas da escola")
        print("1. escreva a sua notas")
        print("2. Lista de notas")
        print("3. Mostrar nota final")
        print("0. Sair")

        opcao = input("Escolhe uma opção: ")

        if opcao == "1":
            inserir_notas()
        elif opcao == "2":
            listar_notas()
        elif opcao == "3":
            media = calcular_media()
            print(f"Média: {media:.2f}")
            print("Classificação:", classificacao(media))
        elif opcao == "0":
            print("Saindo.")
            break
        else:
            print("Opção inválida!")

# Executar o programa
menu()
