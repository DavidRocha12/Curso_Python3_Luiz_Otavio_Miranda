"""
Faça um programa que peça ao usuário para digitar um número
inteiro, informe se este número é par ou impar. Caso o 
usuário não digite um número inteiro, informe que não é um 
número inteiro
"""
try:
    n = input("Digite um número inteiro: ")
    n = int(n)

    if n % 2 == 0:
        print(f"O {n} é Par.")
    else:
        print(f"O {n} é Impar.")

except:
    print("Você não digitou um número inteiro!")
