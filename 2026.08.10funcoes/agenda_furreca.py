import subprocess
import random

def cls():
    subprocess.run("cls", shell=True)

def new_contact():
    pass

def lists_contact():
    pass

def edit_contact():
    pass

def delete_contact():
    pass

# Programa principal
def mains(erro = str()):
    # Main loop
    while True:
        cls()

        print("[ AGENDA FURRECA - MENU PRINCIPAL]")
        if erro:
            print(erro)
        erro = str()
        print('''
Opções
1 - Novo contato
2 - Listar contato
3 - Editar contato
4 - Apaar contato
0 - Sair do programa
''')

