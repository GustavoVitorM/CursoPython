# Desafio 6 - Horário

print("--- SAUDAÇÃO ---")

horario = input("Que horas são? ")

if horario.isdigit():
    horario = int(horario)
    if 0 <= horario < 12:
        print(f"Bom dia! São {horario} horas!")
    elif 12 <= horario < 18:
        print(f"Boa tarde! São {horario} horas!")
    elif 18 <= horario < 24:
        print(f"Boa noite! São {horario} horas!")
    else:
        print("Horário inválido!")
else:
    print("Valor digitado inválido!")