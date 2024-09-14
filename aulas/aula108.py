c =1323

def escopo():
    c = 1

    print(c)
    def escopo2():
        global c
        c = 3
        print(c)
    
    escopo2()
    print(c)


print(c)
escopo()
print(c)
