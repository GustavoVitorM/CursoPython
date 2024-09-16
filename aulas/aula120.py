# Criando dicionário
pessoa = {}

# definindo o valor de uma chave em uma variável
chave = "nome"

# adicionando um valor a lista a partir de uma variável
pessoa[chave] = "Gustavo"
# adicionando um valor a lista sem variável
pessoa["sobrenome"] = "Vitor"

# exibindo um valor da lista usando uma varável
print(pessoa[chave])

# alterando um valor lista a partir de uma chave
pessoa[chave] = "Maria"

# deletando o valor de uma varável
del pessoa["sobrenome"]

#Mostrando a lista
print(pessoa)

# Condição se uma chave existe ou não
if not pessoa.get("sobrenome", None):
    print("Não existe")
else:
    print(pessoa["sobrenome"])

# parametros do método --> chave, resultado se não houver