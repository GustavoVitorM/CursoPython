"""
Higher Order Functions
Funções de Primeira Classe
"""

# Definindo uma função
def saudacao(msg, nome):
    # Retorna a mensagem + nome dos parâmetros
    return f"{msg}, {nome}"

# Definindo outra função - Higher Order Function
def executa(funcao, *args):
    # Retorna uma função com os parâmetros descompactador
    return funcao(*args)

# Exibe o valor gerado pela função executa()
# a partir do 2 valor, os valores entram em *args
print(executa(saudacao, "bom dia", "Gustavo"))