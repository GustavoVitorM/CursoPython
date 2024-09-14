"""
    Validando um cpf
"""
import random

cpf = ''
for _ in range(9):
    cpf += str(random.randint(0, 9))

digitos = cpf.replace(".", "")
digitos = digitos.replace("-", "")
digitos_finais = []

resultado = 0
for i in range(0, 9, 1):
    resultado += int(digitos[i]) * (10 - i)

resultado = (resultado * 10) % 11

if resultado > 9:
    resultado = 0

digitos_finais.append(resultado)

resultado = 0   
for i in range(0, 10, 1):
    resultado += int(digitos[i]) * (11 - i)

resultado = (resultado * 10) % 11

if resultado > 9:
    resultado = 0

digitos_finais.append(resultado)

if digitos_finais[0] == int(digitos[9]) and digitos_finais[1] == int(digitos[10]):
    print("CPF Válido")
else:
    print("CPF Inválido")