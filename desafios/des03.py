"""
Exercício 3

Peça ao usuário para digitar seu nome 
Peça ao usuário para digitar sua idade 
Se o nome e idades forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém {ou não} espaços
        Seu nome tem {n} letras 
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome_usuário = str.lower(input("Digite seu nome:"))
idade_usuário = input("Digite sua idade: ")

if nome_usuário and idade_usuário:
    ctn_espaços = 'não ' if not " " in nome_usuário else ""

    print(f"Seu nome é {nome_usuário};")
    print(f"Seu nome invertido é {nome_usuário[::-1]};")
    print(f"Seu nome {ctn_espaços}contém espaços;")
    print(f"Seu nome tem {len(nome_usuário)} letras;")
    print(f"A primeira letra do seu nome é \"{nome_usuário[0]}\"")
    print(f"A última letra do seu nome é \"{nome_usuário[-1]}\"")
else:
    print("Desculpe, você deixou campos vazios.")
