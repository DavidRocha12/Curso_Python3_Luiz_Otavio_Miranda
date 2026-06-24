"""
Faça um programa que peça o primeiro nome do usuário. Se o nome
tiver 4 letras ou menos escreva "Seu nome é curto", se tiver
entre 5 e 6 letras, escreva "Seu nome é normal", 
maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu primeiro nome: ")

tamanho = len(nome)

if tamanho <= 4:
    print(f"Seu nome tem {tamanho} letras, e é curto!")
elif tamanho <= 6:
    print(f"Seu nome tem {tamanho} letras, e é normal")
else:
    print(f"Seu nome tem {tamanho} letras, e é muito grande!")
