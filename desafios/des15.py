# --- Sistema de perguntas e respostas ---

questions = [
    {
        "question": "Quanto é 3*3?",
        "options": ["3", "5", "10", "9"],
        "answare": "9"
    },
    {
        "question": "Quanto é 102/3?",
        "options": ["34", "12", "32", "45"],
        "answare": "34"
    },
    {
        "question": "Quanto é 1+1?",
        "options": ["1", "85", "2", "6"],
        "answare": "2"
    }
]

for question in questions:
    print("-"*30)
    print(question["question"])
    
    options = question["options"]

    ind = 1
    for i in options:
        print(f"{ind}) {i}")
        ind += 1
    
    while True:
        try:
            answare = int(input("Digite uma das opções: "))
            if 4 > answare < 1:
                print("Resposta inválida! Selecione uma das opções disponíveis!!")
            break
        except:
            print("Resposta inválida! O valor digitado não é um número!")

    if options[answare - 1] == question["answare"]:
        print("Resposta certa!! ")
    else:
        print("Resposta errada!!")
