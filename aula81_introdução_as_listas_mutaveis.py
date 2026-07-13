"""
Introdução sobre as listas mutáveis em Python

Listas  em Python

Tipo list - Mutável

Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

# ......+01234 indices positivos 
# ......-54231 indices negativos

string = "abcde" # 5 caracteres (len)

# Strings são sequências indexadas de caracteres, o que permite acessar cada 
# caractere por seu índice. No entanto, elas são imutáveis e não podem ser modificadas.

# Lista é do tipo mutável - a lista pode ser modificada

# String - sequência imutável de caracteres.
# Lista - sequência mutável de elementos.

# Listas são mutáveis, ou seja, podem ser modificadas.
# É possível acessar cada elemento da lista por meio de índices.
# Cada índice representa a posição de um elemento na lista.
# Cada elemento da lista pode ser modificada, veja o exemplo abaixo:

lista = [123, True, "Luiz Otávio", 1.2, []]
print(lista)
lista[-3] = "Maria"
print(lista)

"""
Resultado:

[123, True, 'Luiz Otávio', 1.2, []]
[123, True, 'Maria', 1.2, []]
"""
# Checando o tipo de um valor em uma lista.

print(lista[2], type(lista[2]))

"""
Resultado

Maria <class 'str'>

"""