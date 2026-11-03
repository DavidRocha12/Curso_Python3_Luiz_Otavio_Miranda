perguntas = [
    {
        "Pergunta" : "Quanto é 2 + 2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta" : "4",
    },
    {
        "Pergunta" : "Quanto é 5 * 5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta" : "25",
    },
    {
        "Pergunta" : "Quanto é 10 / 2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta" : "5",
    }
]

cont = 0
for pergunta in perguntas:
    lista_pergunta = list(pergunta)

    print(f"{lista_pergunta[0]}: {pergunta["Pergunta"]}")
    respostas = pergunta["Opções"]

    print()

    print(f"{lista_pergunta[1]}:")

    for i, valor in enumerate(respostas):
        print(f"{i}) {valor}")

    escolha = input("Escolha uma das opções: ")
    print()

    # Variável para controlar se o usuário acertou 
    acertou = False
    
    # verifica se o usuário digitou um número
    if escolha.isdigit():
        escolha = int(escolha)
        # verifica se o número digitado está dentro das opções válidas (0, 1, 2, 3)
        if escolha >= 0 and escolha < len(respostas):
            # compara a opção escolhida com a resposta correta
            if respostas[escolha] == pergunta["Resposta"]:
                acertou = True

    # Exibe o resiltado se validação
    if acertou:
        print("Você acertou!")
        cont += 1
        print()
    else:
        print("Você errou!")
        print()

print(f"Você acertou {cont} de {len(perguntas)} perguntas!")
