# Questão 3 – Lista de frutas

"""Crie uma lista contendo pelo menos 5 frutas. 

Depois: 

Exiba a lista completa. 

Exiba apenas a primeira fruta. 

Exiba apenas a última fruta. 

Adicione algumas frutas e exiba a última, independentemente da quantidade. 

 """

fruits = [ "banana", "stramberry", "grape", "mango", "cherry"]

print(fruits)
print(fruits[0])
print(fruits[4])

fruits.extend(["apple", "blueberry"])

print(fruits[-1])