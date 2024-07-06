nomes = ["Maria", "Gustavo", "Rosa"]
nomes.append("Lucas")

lista_enumarada = enumerate(nomes)
print(lista_enumarada)
# <enumerate object at 0x00000170FE377060>
print(list(lista_enumarada))
# [(0, 'Maria'), (1, 'Gustavo'), (2, 'Rosa'), (3, 'Lucas')]

# Utilizando em um for
for indice, nome in enumerate(nomes):
    print(indice, nome)
