# Exercício 5 - Par ou Impar

numero = input("Digite um número inteiro: ")

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
else:
    print("Você não digitou um número inteiro.")