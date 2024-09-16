# Declarando uma variável aleatória
c = 1323

# Definindo uma função
def escopo():
    # Escopo local da função
    # Variável com um valor local
    c = 1

    # Valor printado = "1"
    print(c)

    # Definindo mais uma função
    def escopo2():

        # Chamando a variável global para alteração
        global c

        # Mudando valor da variável 
        c = 3

        # Valor printado = 3
        print(c)
    
    # Chamando a função
    escopo2()
    # Valor printado = "1"
    print(c)

# Valor printado = "1323"
print(c)
# Chamando a primeira função
escopo()
# Valor printado = "3"
print(c)
