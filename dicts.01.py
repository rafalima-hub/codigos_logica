produtos = [
    # Forma para usar de base
    {
       "nome":"",
       "codigo":"",
       "preco":0.0,
       "quantidade":0,
       "categoria":""
    },
    {
       "nome":"saia",
       "preco":100.0,
       "codigo":"1234",
       "quantidade":10,
       "categoria":"vestimenta"
    },
    {
       "nome":"colher",
       "codigo":"4321",
       "preco":10.0,
       "quantidade":20,
       "categoria":"utencilhos"
    },
    {
       "nome":"bronzer",
       "codigo":"5678",
       "preco":150.0,
       "quantidade":15,
       "categoria":"cosmetico"
    },
]

print()

# Todos os dados de "Trakinas"
print(produtos[1]["categoria"])

# Todos os produtos
print(produtos)

print("/n-------------/n")

# Todos os produtos usando "for"
for produto in produtos:
   print(f"{produto["nome"]} - R${produto["preco"]}")