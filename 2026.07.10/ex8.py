# Questão 8 – Desconto especial (operador OR)

print()

"""Crie as variáveis: 

idade = 65 

estudante = False 

Uma pessoa recebe desconto se: 

tiver 60 anos ou mais ou 

for estudante. 

Utilize o operador or para verificar essa condição. 

Exiba: 

Tem direito ao desconto. 

ou 

Não tem direito ao desconto. """

idade = 65
estudante = False

if idade >= 60 and estudante: # Não é necessário colocar '== True' pois a variável com boole sempre será True.
    print("Tem direito ao desconto.")
else:
    print("Não tem direito ao desconto.")