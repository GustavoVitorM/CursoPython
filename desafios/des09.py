letras = ""
resposta = "menos"

print("---- Bem Vindo ao Jogo de adivinhação ----")

while True:
    
    print("-"*20)
    letra = input("Digite um caracter: ")
    if len(letra) != 1:
        print("Digite apenas um caracter!")
        continue
    
    if letra in letras:
        print("Essa letra já foi digitada! Tente novamente!")
        continue

    palavra = ""
    letras += f"{letra}-"
    
    for l in resposta:
        if l in letras:
            palavra += l 
        else:
            palavra += "*"
        
    if resposta == palavra:
        break

    print("Resposta:", palavra)

    print("Letras já digitadas: ")
    print(letras)


print(f"Parabéns! Você descobriu! A palavra era '{palavra}'")
