"""
Introdução ás funções

Funções são trechos de código usados para replicar
determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""

print("Várias") # - print é uma função do python

# Criando uma função

def Print():# o correto é fazer os nomes da funções com letras minúsculas
    print("Várias")# -Seria um item que seria utilizados várias vezes

Print()

# Função com paramétros para receber argumentos:

def imprimir(a, b, c):
    print(a, b, c)

a = 1
b = 2
c = 3
imprimir(a, b, c)# recebendo variáveis o argumentos diretamente, podendo
# receber o que você desejar, lembrando que a função vai ser feita
# para uma tarefa especifica.

# Função de saudação

def saudacao(nome="sem nome"): # se caso não receber nada vai escrever sem nome
    print(f"Olá {nome}")

saudacao()
saudacao("David")
