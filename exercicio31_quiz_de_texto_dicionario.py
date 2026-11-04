filmes = [
    {
        "Pergunta": "Qual é o nome do robô que compacta lixo na Terra?",
        "Resposta": "wall-e"
    },
    {
        "Pergunta": "Quem é o vilão principal do primeiro filme dos Vingadores?",
        "Resposta": "loki"
    },
    {
        "Pergunta": "Qual o nome do peixe palhaço que se perde no oceano?",
        "Resposta": "nemo"
    }
]

certo = 0
for pergunta in filmes:
    print(f"Pergunta: {pergunta["Pergunta"]}")
    resposta_usuario = input("Sua resposta: ").lower().strip()

    nome_real = False
    if not resposta_usuario.isnumeric():
        if resposta_usuario == pergunta["Resposta"]:
            nome_real = True
    else:
        print("Errou, Digite somente nomes!")
        continue

    if nome_real:
        print("Você Acertou!")
        certo += 1
    else:
        print("Você Errou!")

    print("-" * 30)

    print()
print(f"Fim do jogo, Você fez {certo} ponto(s).")