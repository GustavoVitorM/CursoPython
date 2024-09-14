import decimal

# O decimal so é necessário utilizar se for preciso ter 
# o valor muito avançado de casas decimais
# Documento sobre pontos flutuantes nas linguágens:
# https://docs.python.org/pt-br/3/tutorial/floatingpoint.html

numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.2)
numero_3 = numero_1 + numero_2
print(f"{numero_3}")