"""
    Closure e fuções que retornam outras funções
"""

# criação de uma função
def criar_saudacao(saudacao):
    # Definindo uma nova função
    def saudar(nome):
        return f"{saudacao}, {nome}"
    # Retorna a função saudar - Closure
    return saudar

# Guarda uma função que será utilizada futuramente.
falar_bom_dia = criar_saudacao("Bom dia")
falar_boa_noite = criar_saudacao("Boa noite")

# Loop com uma lista de nomes
for nome in ['Maria', "João", "Marcos"]:
    print("-"*5)
    # Exibe o resultado da função guardada anteriormente
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))