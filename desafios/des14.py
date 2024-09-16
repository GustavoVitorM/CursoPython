
# Duplicando, Triplicando e Quadruplicando valores 
# utilizando closure

def equ(mult):
    def multi(value):
        return value * mult
    return multi

duplicando = equ(2)
triplicando = equ(3)
quadruplicando = equ(4)

print(duplicando(2))
print(triplicando(2))
print(quadruplicando(2))
