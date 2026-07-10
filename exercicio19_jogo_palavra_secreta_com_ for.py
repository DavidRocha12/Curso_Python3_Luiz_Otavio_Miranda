"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.

- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.

    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.

Faça a contagem de tentativas do seu usuário.
"""
import os

palavra_secreta = "perfume"
letra_certa = ""
contagem = 0
while True:
    letra = input("Digite uma letra: ")

    contagem += 1

    if len(letra) > 1:
        print("Digite apenas uma letra!")
        continue

    if letra in palavra_secreta:
        letra_certa += letra

    palavra_certa = ""
    for lt in palavra_secreta:
        if lt in letra_certa:
            palavra_certa += lt
        else:
            palavra_certa += "*"

    os.system("clear")

    print(palavra_certa)

    if palavra_certa == palavra_secreta:
        print(f"Tentativas: {contagem}")
        print(f"Parabéns, você completou a palavra_secreta que é {palavra_secreta}!")
        break
