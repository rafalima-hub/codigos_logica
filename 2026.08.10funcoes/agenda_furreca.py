###############################################
# 2026.08.10.Funcoes/agenda_furreca.py        #
# AGENDA FURRECA.py                           #
# Versão 2026.08.10                           #
# By Rafa Lima - https://github.xonm/rafalima #
###############################################

# Bibliotecas
import subprocess
import os
import json

# "random" e para gerar numeros aleatorios
import random

# Banco de dados em memoria (dict) (Moch)
database = {}


def save_database():
    with open("database.jason", "w", encoding="utf-8") as file:
        # 'jdon.dump' transforma o dict em JSON e grava no arquivo
        json.dump(database, file, indent=4, ensure_ascii=False)

def load_database():
    global database

    # O try/except é só para o primeiro uso do programa
    try:
        with open("database.json", "r", encoding="utf-8") as file:
            database = json.load(file)
    except FileNotFoundError:
        database = {}

def cls():
    # Limpa tela
    if os.name == "nt":
        # Se o sistema for Windows
        subprocess.run("cls", shell=True)
    else:
        # Se o sistema for Linux ou MacOS
        subprocess.run("clear", shell=True)


def new_contact():
    # Cadastrar novos contatos
    cls()

    print("------------------------------------")
    print("|  AGENDA FURRECA - NOVOS CONTATOS |")
    print("------------------------------------")
    print("\nDigite os dados do contato:\n")
    print("------------------------------------")

    while True:
        name = input(" • Nome: ")
        if name.strip() != "":
            break
        print("-----", "Digite um nome válido!", "-----")

    while True:
        contact = input(" • Contato: ")
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
    save_database()

    print("------------------------------------")

    print(f"\nUsuáriocom ID {key} adicionado!")
    input("Tecle [Enter] para continuar")

    main()

def list_contact():
    # Lista todos os registros
    cls()

    # Cabeçalho
    print("------------------------------------")
    print("|  AGENDA FURRECA - LISTAR CONTATOS |")
    print("------------------------------------")
    print()
    print("   ", len(database), "usuários encontrados!")
    print()
    print("------------------------------------")

    # Loop para iterar os registros usando o método 'dict.items()'
    for key, value in database.items():
        # Formata saídas
        print("ID", key)
        print(" • Nome:", value['name'])
        print(" • Contato:", value['contact'])
        print()


    print("------------------------------------")
    input("Tecle [Enter] para continuar")
    main()

def edit_contact():
    cls()

    print("------------------------------------")
    print("|  AGENDA FURRECA - EDITA CONTATO  |")
    print("------------------------------------")

    print()
    print("------------------------------------")
    while True:
        key = input("Digite o Id do usuário: ")
        if key in database:
            break
        print("-----", "ID não encontrado", "-----")

    print()
    print("ID", key)
    print(" • Nome:", database[key]['name'])
    print(" • Contato:", database[key]['contact'])
    print()
    print("------------------------------------")

    print("Digite os novos dados:")


    while True:
        name = input(" • Nome: ")
        if name.strip() != "":
            break
        print("-----", "Digite um nome válido!", "-----")

    while True:
        contact = input(" • Contato: ")
        if contact.strip() != "":
            break
        print("Digite um contato válido!")

    database[key] = dict(name=name, contact=contact)

    print()
    print("Contato atualizado")
    print("Tecle [Enter] para continuar")
    main()

def delete_contact():
    cls()

    print("------------------------------------")
    print("|  AGENDA FURRECA - APAGA CONTATO  |")
    print("------------------------------------")

    print()
    print("------------------------------------")
    while True:
        key = input("Digite o Id do usuário: ")
        if key in database:
            break
        print("-----", "ID não encontrado!", "-----")

    print()
    print("------------------------------------")
    print("ID: ", key)
    print(" • Nome:", database[key]['name'])
    print(" • Contato:", database[key]['contact'])
    print()

    option = input("Tem certeza que deseja apagar [S/N]? ")
    if option.upper() == "S":
        del database[key]
        save_database()
        print("Contato apagado!")
    else:
        print()
        print("Não aconteceu nada!")

    input("Tecle [Enter] para continuar")
    main()

def main(erro=str()):
    # Programa principal e "main loop"
    while True:
        # Limpa tela
        cls()

        # Cabeçalho
        print("------------------------------------")
        print("|  AGENDA FURRECA - MENU PRINCIPAL |")
        print("------------------------------------")

        # Exibe menu principal
        print('''
Escolha uma das seguintes opções:
---------------------------------
Tecle 1 - Novo contato
Tecle 2 - Listar contato
Tecle 3 - Editar contato
Tecle 4 - Apagar contato
Tecle 0 - Sair do programa
---------------------------------
''')

        # Exibe mansagem de erro se existir
        if erro:
            print("-----", erro, "-----")

        # Recebe opção do usuário
        opcao = input("Qual opção você deseja? ")

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


# Carrega o banco de dados
load_database()

# "Roda" o programa de novo
main()