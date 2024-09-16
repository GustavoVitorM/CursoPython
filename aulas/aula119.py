"""
Dicionários em Python
- São estruturas de dados do tipo par de "Chave" e "Valor"
- Chaves == "Índice" da lista
- O valor pode ser de qualquer tipo, incluindo outro dicionário
- Utiliza-se chaves - {} - ou a classe dict para sua definição
- Imutáveis: str, int, float, bool, tuple
- Mutável: dict, list
------
pessoa = {
    "nome": 'Gustavo',
    "sobrenome": "Vitor",
    "idade": 18,
    "altura": 1.80,
    "endereços": [
        {"rua": "exemplo". "número": 812},
        {"rua": "monte azul". "número": 3523}
    ]
}
"""

# Criando uma lista - 1 forma
pessoa = {
    "nome": 'Gustavo',
    "sobrenome": "Vitor",
    "idade": 18,
    "altura": 1.80,
    "endereços": [
        {"rua": "exemplo", "número": 812},
        {"rua": "monte azul", "número": 3523}
    ]
}


# Criando uma lista - 2 forma
pessoa2 = dict(nome="Luiz Gustavo", sobrenome="Martins")

# mostando os valores a partir da chave
for chave in pessoa:
    print(chave, "-->", pessoa[chave])