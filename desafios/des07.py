# Desafio 7 - Tamanho do nome

print("--- Analizando seu nome ---")

nome = input("Qual seu primeiro nome? ")

if 0 < len(nome) <= 4:
    print("Seu nome é curto!")
elif 4 < len(nome) < 6:
    print("Seu nome é normal!")
elif 6 < len(nome):
    print("Seu nome é muito grande!")
else:
    print("Você não digitou nada!")
