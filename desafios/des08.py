# Pojeto Calculadora com while

cont = 0

while True:
    print("---- Calculadora ----")
    if cont == 0:
        n1 = input("-> Digite um número inteiro: ")

    print("Operadores disponíveis\n",
          " + (Adição), - (subtração),\n",
          " * (multiplicação), / (Divisão)", sep="")
    operador = input("-> Digite o operador: ")

    n2 = input("-> Digite o segundo número: ")
    
    try:
        n1 = int(n1)
        n2 = int(n2)

        if operador == "+":
            resultado = n1 + n2
        elif operador == "-":
            resultado = n1 - n2
        elif resultado == "*":
            resultado = n1 * n2
        elif resultado == "/":
            resultado = n1 / n2
        else:
            print("O operador digitado é inválido!")

        print("-"*15)
        print(f"Sua conta ficou {n1} {operador} {n2}")
        print(f"Resultado: {resultado}")
        print("-"*15)
        
        while True:
        
            continuar = input("Quer utilizar o resultado dessa conta? (S/N/Sair)").lower()
        
            if continuar == "s":
                n1 = resultado
                cont = 1
                break
            elif continuar == "n" or continuar == "sair":
                cont = 0
                break
            else:
                print("Digite uma opção válida! ")
        
        if continuar == "sair":
            break

    except:
        print("-"*15)
        print('Você não difgitou um número ou \n',
              'digitou um operador inválido! \n',
              'Tente novamente!', sep="")
        print("-"*15)

