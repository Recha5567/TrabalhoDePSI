print("_____Bem vindo ao gerador_____")

print("1 - Gerar siglas")
print("2 - Gerar código")
print("3 - Gerar password")
print("4 - Gerar tudo")

opcao = input("Escolhe uma opção: ")
print("Não escreveste nada, tenta outra vez!")

palavra = input("Escreva alguma coisa:").strip()
if not palavra:
    print("Não escrevdeu nada intruduza alguma coisa.")
    while True:
        palavra = input("Escreva alguma coisa: ").strip()
        if palavra:
            break
        print("Não escreveste nada, tenta outra vez!")

palavras = palavra.split()


sigla1 = ""
for p in palavras:
    sigla1 += p[0].upper()

sigla2 = ""
for p in palavras:
    sigla2 +=p[:2].upper()

codigo = sigla1 + str(len(palavra))
password = sigla1.lower() + "@" + str(len(palavras))
import random
import string

if opcao == "1":
    print("Resultados das gerações :)")
    print("sigla 1:", sigla1)
    print("sigla 2:", sigla2)
    print("Obrigado por usar o meu gerador ^-^")
elif opcao == "2":
    print("Resultados das gerações :)")
    print("codigo 2:", codigo)
    print("Obrigado por usar o meu gerador ^-^")
elif opcao == "3":
    print("Resultados das gerações :)")
    print("password:" , password_forte)
    print("Obrigado por usar o meu gerador ^-^")
elif opcao == "4":
    print("Resultados das gerações :)")
    print("Sigla 1:", sigla1)
    print("sigla 2:", sigla2)
    print("Código:", codigo)
    print("Password:", password)
    print("Obrigado por usar o meu gerador ^-^")
