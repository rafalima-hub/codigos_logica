###############################################
# 2026.08.10.Funcoes/agenda_furreca.py        #
# AGENDA FURRECA.py                           #
# Versão 2026.08.10                           #
# By Rafa Lima - https://github.xonm/rafalima #
###############################################

import subprocess
import os
import random

database = {
    "1": {"name": "Joca da Silva", "contact":"(21) 9988123456"},
    "120": {"name": "Maria Sarilampo","contact": "mari@mail.com.br"}
}

def cls():
    # Limpa tela
    if os.name == "nt":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

def new_contact():
    cls()

    print("[ AGENDA FURRECA - MENU PRINCIPAL ]")
    print("\nDigite os dados do contato:\n")

    while True:
        name = input(" - Nome: ")
        if name.strip() != "":
            break
        print("-----", "Digite um nome válido!", "-----")

    while True:
        contact = input(" - Contato: ")
        if contact.strip() != "":
            break
        print("Digite um contato válido!")

    # Gera o ID aleatório e não repetido
    while True:
        key = str(random.randint(1, 1000))
        if key not in database:
            break

    # Salva o novo cadastro no formato "dict"
    database[key] = dict(name=name, contact=contact)

    print(f"\nUsuáriocom ID {key} adicionado")
    input("Tecle [Enter] para continuar")

    main()

def list_contact():
    # Lista todos os regisros
    cls()

    # Cabeçalho
    print("[ AGENDA FURRECA - MENU PRINCIPAL ]")
    print()
    print(len(database), "usuários encontrados!")
    print()

    # Loop para iterar os registros usando o método 'dict.items()'
    for key, value in database.items()
        # Formata saídas
        print("ID", key)
        print(" - Nome:", value['name'])
        print(" - Contato:", value['contact'])
        print()

        input("Tecle [Enter] para continuar")

        main()

def edit_contact():
    cls()
    
    print("[ AGENDA FURRECA - MENU PRINCIPAL ]")

    print()
    while True:
        key = input("Digite o Id do usuário: ")
        if key in database:
            break
        print("-----", "ID não encontrado", "-----")

    print()
    print("ID", key)
    print(" - Nome:", database[key]['name'])
    print(" - Contato:", database[key]['contact'])
    print()

    print("Digite os novos dados:")

    while True:

def delete_contact():
    cls()
    
    print("[ AGENDA FURRECA - MENU PRINCIPAL ]")
    print()


def main(erro=str()):
    # Programa principal e "main loop"
    while True:
        # Limpa tela
        cls()

        # Cabeçalho
        print("[ AGENDA FURRECA - MENU PRINCIPAL ]")

        # Exibe menu principal
        print('''
Opções
1 - Novo contato
2 - Listar contato
3 - Editar contato
4 - Apaar contato
0 - Sair do programa
''')

        # Exibe mansagem de erro se existir
        if erro:
            print("-----", erro, "-----")

        # Recebe opção do usuário
        opcao = input("Escolha uma opção: ")

        # Execulta a opção seçecionada
        match opcao:
            case "1":
                new_contact()
            case "2":
                list_contact()
            case "3":
                edit_contact()
            case "4":
                delete_contact()
            case "0":
                # Limpa a tela, exibe confirmação e termina o programa
                cls()
                print("\nAcabou")
                exit()
            case _:
                # Se escolheu uma opção inválida, chama o menu novamente
                erro = "Digite uma opção válida!"
                main()


# "Roda" o programa de novo
main()