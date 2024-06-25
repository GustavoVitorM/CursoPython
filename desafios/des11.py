import os

compras = []

while True:
    os.system("clear")
    print(f"{' Bem vindo a sua lista de compras ':-^50}")
    print("O que deseja fazer?")
    print("< 1 > INSERIR ITEM --\n",
          "< 2 > APAGAR ITEM ---\n",
          "< 3 > LISTAR ITENS --\n",
          "< 4 > Sair ----------\n", sep='')
    
    opção = input("Digite uma opção: ")
    
    os.system("clear")
    try:
        opção = int(opção)
    except:
        print("Opção digitada inválida! Tente novamente!")
    if opção == 1:
        print(f"{' Adicionar item ':-^20}")
        item = input("Digite o item:")
        compras.append(item)
    elif opção == 2:
        print(f"{' Apagar item ':-^20}")
        item = input("Digite o item:")
        if item in compras:
            compras.remove(item)
        else:
            print("Esse item não consta na lista!")
    elif opção == 3:
        print(f"{' Lista de Itens ':-^20}")
        for i in compras:
            print(f'--> {i}')
        print(f"{"-"*20}")

        continuar = input("")
    elif opção == 4:
        break

        