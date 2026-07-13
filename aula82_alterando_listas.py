"""
Métodos úteis:

append, insert, pop, del, clear, extend, +

Create Read Update Delete
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40]
# pegando um valor
numero = lista[2]
print(numero)
# Modificando elemento da lista
lista[2] = 300
print(lista)
# Deletando elemento especifico da lista
del lista[2]
print(lista)# os indices automaticamentes serão ajustados
# indice 0 - 10, 1 - 20, 2 - 40 
# o 30 que estava no indice 2 foi apagado, 
# então o indice do elemento 40 se tornou 2, ajustando os indices conforme
# os elementos dentro da lista.
 
# Adicionando elemento ao final da lista
lista.append(50)
print(lista)
# Removendo o ultimo elemento
lista.pop()
print(lista)

"""
Resultado:

30
[10, 20, 300, 40]
[10, 20, 40]
[10, 20, 40, 50]
[10, 20, 40]
"""
