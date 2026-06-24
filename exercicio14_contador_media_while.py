"""
1. O Contador de Números e Média (Análise de Dados)

Objetivo: Criar um programa que receba vários números inteiros do usuário até que ele digite 
um número específico para parar. No final, o programa mostra estatísticas sobre os números digitados.

Regras:

O loop while deve rodar até que o usuário digite 0 (condição de parada).

O programa deve contar quantos números foram digitados (sem incluir o 0).

O programa deve somar todos os números e, no final, exibir a média aritmética deles.

Tratamento extra: Se o usuário digitar 0 logo de primeira, exiba uma mensagem dizendo
que nenhum número foi computado (evitando divisão por zero na média!).
"""

print("Contador de Números e Média")
print("-" * 28)

print()

contador = 0
soma = 0
try:
    while True:
        try:
            usuario = float(input("Digite um numero, para finaliza digite '0': "))
        except ValueError:
            print("Digite apenas números!")
            print()
            continue
        
        print()

        if usuario < 0:
            print("Número negativo ignorado!")
            continue
       
        if usuario == 0:
            print("Finalizando programa!\n")
            break

        contador += 1
        soma += usuario

    media = soma / contador

    print(f"Você digitou {contador} numeros, somando eles o valor é {soma}, e a média desse valor é {media}")
except ZeroDivisionError:
    print("Nenhum número foi digitado!")
