# Questão 5 – Sistema de notas 

"""Crie uma variável chamada nota. 

Utilize if...elif...else para classificar: 

Nota 

Resultado 

9 a 10 

Excelente 

7 a 8.9 

Aprovado 

5 a 6.9 

Recuperação 

Menor que 5 

Reprovado 

"""

nota = 4.0

if nota >= 9.0:
    print("Excelente")
elif nota >= 7.0:
    print("Aprovado")
elif nota >= 5.0:
    print("Recuperação")
else:
    print("Reprovado")