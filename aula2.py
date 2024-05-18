#Função print()

'''
    print() é um comando usado para escrever uma informação na tela,
    dentro dos parênteses ele requer alguns parâmetros, como o que sera
    escrito, e os argumentos 'sep=""' e 'end=""'.
    --> sep="" - Altera o que separa dois dados do print, por exemplo:
        print(12, 34, sep="##") -> nesse caso ele possui 2 dados mais
        o separador inserindo "##" entre eles, escrevendo: 
        -> 12##34
        O padrão desse argumento é um espaço simples.
    --> end="" - Altera o que estara no final dos argumentos, exemplo:
        print(56, 78, end="#\n") - nesse caso ao escrever ambos os dados
        escreverá uma # e quebrará a linha, escrevendo:   
        -> 56 78#
        ->
        O padrão é uma quebra de linha comum
    --> \n - é um comando para quebra de linha.
'''

print(12, 34, sep="##")
print(56, 78, end="#\n")