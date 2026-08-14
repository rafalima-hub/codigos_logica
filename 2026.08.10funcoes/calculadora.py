import os
import subprocess

def cls():
    # Limpa tela
    if os.name == "nt":
        # Se o sistema for Windows
        subprocess.run("cls", shell=True)
    else:
        # Se o sistema for Linux ou MacOS
        subprocess.run("clear", shell=True)

# Utilizado para soma
def adicao():
    # Limpa tela
    cls()

    # Cabeçalho
    print("------------------------")
    print("| CAUCULADORA - ADIÇÃO |")
    print("------------------------")
    print()

    while True:
        try:
           val1 = float(input("\nDigite a primeira parcela: "))
           break
        except FloatingPointError:
            print("Valor inválido!")
            continue

    while True:
            try:
               val2 = float(input("\nDigite a segunda parcela: "))
               break
            except FloatingPointError:
                print("Valor inválido!")
                continue

    # Operação
    resultado = val1 + val2
    print("O resultado da sua adição é", resultado, "!")

    input("Tecle [Enter] para continuar...")
    main()

def subtracao():
    cls()

    print("---------------------------")
    print("| CAUCULADORA - SUBTRAÇÃO |")
    print("--------------------------")
    print()

    while True:
            try:
               val1 = float(input("Digite a primeira parcela: "))
               break
            except FloatingPointError:
                print("Valor inválido!")
                continue

    while True:
            try:
               val2 = float(input("Digite a segunda parcela: "))
               break
            except FloatingPointError:
                print("Valor inválido!")
                continue

    # Operação
    resultado = val1 - val2
    print("O resultado da sua subtração é", resultado, "!")

    input("Tecle [Enter] para continuar...")
    main()

def divisao():
    cls()

 # Cabeçalho
    print("------------------------")
    print("| CAUCULADORA - DIVISÃO |")
    print("------------------------")
    print()

    val1 = float(input("Digite a primeira parcela: "))
    val2 = float(input("Digite a segunda parcela: "))

    # Operação
    while True:
        if val1 != 0 and val2 != 0:
            resultado = val1 / val2
            break
        else:
            print("Número inválido")

    print("O resultado da sua divisão é", resultado, "!")

    input("Tecle [Enter] para continuar...")
    main()

def multiplicacao():
    cls()

    val1 = float(input("Digite a primeira parcela: "))
    val2 = float(input("Digite a segunda parcela: "))

     # Operação
    resultado = val1 * val2
    print("O resultado da sua multiplicação é", resultado, "!")
    
    input("Tecle [Enter] para continuar...")
    main()

def main(erro=str()):
    # Limpa tela
    cls()

    # Cabeçalho
    print("------------------------")
    print("|  CAUCULADORA - MENU  |")
    print("------------------------")
    print()
    print("""
Olá! Para fazer seus calculos, escolha umas das opções abaixo
--------------------------------------------------------------
A - Adição
S - Subtração
D - Divisão
M - Multiplicação
--------------------------------------------------------------
""")

    # Caso tenha erro irá exibir uma mensagem
    if erro:
        print("-----", erro, "-----")

    opcao = input("Qual operação você deseja utilizar? ")
    

    match opcao.upper():
        case "A":
            adicao()
        case "S":
            subtracao()
        case "D":
            divisao()
        case "M":
            multiplicacao()
        case _:
            # Se escolher uma opção inválida chama o menu denovo
            erro = "Digite uma opção válida!"
            main()

main()