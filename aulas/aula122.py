# Métodos úteis dos dicionários em Python
# len - quantidade
# keys - iterável com as chaves
# values - iterável vom os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópiaa rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um titem com a chave especificada (del)
# popitem - Apaga o últipo item adicionado
# update - Atualiza um dicionário com outro


# --- copy ----

# quando uma variável recebe um dicionário, ele não cria uma cópia
# mas referencia o mesmos valores.
# Se alterar o segundo dicionário também altera o segundo

d1 = {
    "c1": 1,
    "c2": 2
}

d2 = d1

d2["c1"] = 100
print(d2, d1)

print("-"*40)

# --- Shallow copy ---
# Mas utilizando o método .copy() ele somente cria uma cópia alternativa
# Mesmo assim é uma cópia rasa, que só aceita alterações na primeira lista

d1 = {
    "c1": 1,
    "c2": 2
}

d2 = d1.copy()

d2["c1"] = 100
print(d2, d1)
