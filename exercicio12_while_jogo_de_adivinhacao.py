"""
3. Jogo da Adivinhação com Dicas e Desistência
Objetivo: O programa escolhe um número secreto e o usuário tenta adivinhar, mas ele pode desistir digitando um número específico.

Regras:

Defina um número secreto (ex: 42).

O while deve rodar enquanto o palpite for diferente do número secreto e o usuário não tiver digitado -1 (que é o código para desistir).

Dentro do loop, use if/elif/else para dizer se o palpite foi "Muito alto", "Muito baixo" ou se ele acertou.

Use operadores booleanos para verificar se o palpite é válido (ex: menor que 0 e diferente de -1 deve dar erro).
"""

numero_secreto = 42
palpite = 0
sair = -1
while palpite != numero_secreto:
    try:
        palpite = int(input("Digite o seu palpite: "))
    except ValueError:
        print("Digite somente números!")
        continue
    
    if palpite == sair:
        print("Finalizando jogo!")
        break

    if palpite < 0 and palpite != sair:
        print("Palpite inválido!")
    elif palpite > numero_secreto:
        print("O número é menor, tente novamente!")
    elif palpite < numero_secreto:
        print("O número é maior, tente novamente!")
    else:
        print("Parabéns, você acertou!")

    print()
    