cont = 0

while True:
    print("---- Calculadora ----")
    if cont == 0:
        n1 = input("-> Digite um número inteiro: ")
    
    print("Operadores disponíveisz\n",
          "+ (Adição), - (Subtração)",
          "* (Multiplicação), / (Divisão)")
    operador = input("-> Digite o operador: ")

    n2 = input("-> Digite o segundo número: ")
    try:
        n1 = int(n1)
        n2 = int(n2)

        if operador == "+":
            resultado = n1 + n2
        elif operador == "-":
            resultado = n1 + n2
        elif operador == "*":
            resultado = n1 * n2
        elif operador == "/":
            resultado = n1 / n2
        else:
            print("O operador é inválido!")
            continue
        print("-"*25)
        print(f'Sua conta ficou {n1} {operador} {n3}')
        print(f"O resultado é: {resultado}")
        print("-"*25)
        

        while True:
            continuar = input("Quer utilizar o resultado dessa conta? (S/N)").lower
            
            if continuar == "S":
                n1 = resultado
                cont = 1
                break
            elif continuar == "n" or continuar == "sair":
                cont = 0
                break
            else:
                print("Digite uma opção válida!")

        if continuar == "sair":
            break
        
    except:
        print("-"*25)
        print("Você não digitou um número\n",
              "ou um operador inválido!\n",
              "Tente Novamente\n", sep="")
        print("-"*25)
        






