"""
O Transformador Universal (Custom Map)

Você já construiu o seu próprio filter. Agora você vai construir o seu próprio map. 
Em vez de filtrar, essa função vai aplicar uma regra matemática para transformar todos os itens da lista.

O que você deve fazer:

Crie duas funções simples: dobrar(numero) (que retorna o número * 2) 
e somar_dez(numero) (que retorna o número + 10).

Crie uma função de alta ordem transformar_lista(lista, regra).

Ela deve criar uma lista nova, passar por cada item da lista original com um for, 
aplicar a regra no item, e guardar o resultado na lista nova. Retorne a lista nova no final.
"""

def dobrar(numero):
    return numero * 2


def somar_dez(numero):
    return numero + 10


def transformar_lista(lista, regra):
    lista_nova = []
    for valor in lista:
        lista_nova.append(regra(valor))
    return lista_nova


numeros = [1, 2, 3, 4]
print(transformar_lista(numeros, dobrar))
print(transformar_lista(numeros, somar_dez))
