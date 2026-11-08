"""
A Calculadora Dinâmica (Higher Order Function)
O objetivo aqui é criar uma função principal que não sabe fazer contas, 
ela apenas delega o trabalho para outras funções que você passar para ela.

O que você deve fazer:

Crie duas funções simples: somar(a, b) e multiplicar(a, b).

Crie uma função de alta ordem chamada calcular(num1, num2, operacao).

A função calcular deve usar a função operacao para processar num1 e num2 e retornar o resultado.
"""

def soma(n_1, n_2):
    soma = n_1 + n_2
    return soma


def multiplica(n_1, n_2):
    mult = n_1 * n_2
    return mult


def calcular(num1, num2, operacao):
    return operacao(num1, num2)


print(calcular(10, 5, soma))
print(calcular(10, 5, multiplica))
