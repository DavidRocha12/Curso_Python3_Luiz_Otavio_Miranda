"""
 Higher Order Funtions

Em Python, uma Higher-Order Function (Função de Ordem Superior ou Função de 1º classe)
é uma função que faz pelo menos uma de duas coisas:

Aceita uma ou mais funções como argumento.

Retorna uma função como resultado.

Isso é possível porque, em Python, as funções são tratadas 
como "cidadãos de primeira classe" (first-class citizens).
Isso significa que uma função pode ser atribuída a uma variável, 
armazenada em estruturas de dados (como listas ou dicionários),
e  passada de um lado para o outro exatamente como você faria 
com um número ou uma string.

Aqui estão os cenários onde elas aparecem:

1. Recebendo uma função como argumento

Você pode criar suas próprias funções que aceitam outras
funções para determinar seu comportamento:
 """

def gritar(texto):
	return texto.upper()


def sussurrar(texto):
	return texto.lower()


# Esta é a Função Higher-Order Function
def aplicar_formatacao(funcao_formatadora, texto):
	return funcao_formatadora(texto)


print(aplicar_formatacao(gritar, "Olá Mundo"))
print(aplicar_formatacao(sussurrar, "Olá Mundo"))

# Resultado:

# OLÁ MUNDO
# olá mundo

"""
Academicamente, os termos Higher Order Functions e First-Class Functions 
têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras
funções

First-Class Functions - Funções que são tratadas como outros tipos 
de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe 
informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo 
significado.
"""

# 2. Funções embutidas (Built-ins)
# Python já vem com várias Higher-Order Functions nativas muito 
# utilizadas, geralmente em conjunto com funções anônimas (lambda):

# map(funcao, iteravel): Aplica uma função a todos os itens de uma lista.

numeros = [1, 2, 3, 4]
quadrados = list(map(lambda x: x**2, numeros))

print(quadrados)

# quadrados = [1, 4, 9, 16]

# filter(funcao, iteravel):  Filtra os itens de uma lista usando uma função que retorna Verdadeiro ou Falso.

numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)

# pares = [2, 4]

# 3. Retornando uma função como resultado
# Higher-Order Functions também podem gerar e 
# devolver novas funções. Esse é o princípio 
# fundamental por trás de Closures e Decorators em Python.

# Esta é a Higher-Order Function
def criar_multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    
    return multiplicar # Retorna a função de dentro, sem executá-la

dobrar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)

print(dobrar(5))   # Saída: 10
print(triplicar(5)) # Saída: 15
