"""
    Validando um cpf
"""

cpf = input("Digite o CPF: ")

separação1 = cpf.split("-")
separação2 = separação1[0].split(".")
digitos = []

for digito in separação2:
    digitos.append(digito[0])
    digitos.append(digito[1])
    digitos.append(digito[2])

resultado = 0
for i in range(0, 9, 1):
    resultado += int(digitos[i]) * (10 - i)

resultado = (resultado * 10) % 11

if resultado > 9:
    resultado = 0

print("DIGITO1: ", resultado)
digitos.append(resultado)

resultado = 0
for i in range(0, 10, 1):
    resultado += int(digitos[i]) * (11 - i)

resultado = (resultado * 10) % 11

if resultado > 9:
    resultado = 0

print("DIGITO 2: ", resultado)