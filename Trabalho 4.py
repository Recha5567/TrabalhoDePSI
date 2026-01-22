# Aplicação para análise de notas

# Função para ler um número inteiro positivo
def ler_inteiro(mensagem):
    while True:  # Repete até o utilizador escrever um valor válido
        valor = input(mensagem)  # Pede um valor ao utilizador
        if valor.isdigit() and int(valor) > 0:  # Verifica se é inteiro positivo
            return int(valor)  # Converte e devolve o número
        print("Escreva um número válido.")  # Mensagem de erro

# Função para ler uma nota (número com ou sem casas decimais)
def ler_nota(mensagem):
    while True:  # Repete até ser introduzida uma nota válida
        valor = input(mensagem)  # Pede a nota ao utilizador
        if valor.replace(".", "", 1).isdigit():  # Verifica se é um número
            return float(valor)  # Converte e devolve a nota
        print("Escreva uma nota válida.")  # Mensagem de erro

# Ciclo principal do programa (repete enquanto o utilizador quiser)
while True:
    notas = []  # Lista para guardar as notas

    # Pede ao utilizador o número de notas
    total = ler_inteiro("Escreva o número de notas que quer colocar: ")

    # Lê cada nota e guarda na lista
    for i in range(1, total + 1):
        notas.append(ler_nota(f"Nota {i}: "))

    # Mostra todas as notas introduzidas
    print("\nNotas introduzidas:")
    for nota in notas:
        print(nota)

    # Mostra os resultados finais
    print("\nResultados finais:")
    print("Nota mais alta:", max(notas))      # Maior nota
    print("Nota mais baixa:", min(notas))     # Menor nota
    print("Média:", sum(notas) / len(notas))  # Média das notas

    # Pergunta se o utilizador quer repetir o programa
    if input("\nENTER para repetir OU outra tecla + ENTER para sair: ") != "":
        break  # Sai do ciclo

# Mensagem final do programa
print("Programa encerrado.")
