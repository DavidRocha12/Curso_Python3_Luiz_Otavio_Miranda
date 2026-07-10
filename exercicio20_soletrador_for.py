"""
Exercício gerado por inteligência artificial

Exercício 1: O Soletrador (Foco no in)
Desafio:
Crie um programa que receba uma palavra guardada em uma variável (por exemplo, palavra = "Aprender").
Use o laço for com o in para percorrer cada letra dessa palavra e imprimi-la na tela em letras maiúsculas,
adicionando um pequeno texto antes.

Exemplo de saída esperada:

Plaintext
Analisando a letra: A
Analisando a letra: P
Analisando a letra: R
...
Dica: O Python permite que você use o for diretamente em um texto (string), tratando cada caractere como um item! 
Para deixar a letra maiúscula na hora de imprimir, você pode usar o método .upper() (ex: letra.upper()).
"""

palavra = "Aprender"

for letra in palavra:
    print(f"Analisando a letra: {letra.upper()}")

print("Palavra analisada!")