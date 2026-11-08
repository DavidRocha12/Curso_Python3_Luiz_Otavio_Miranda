"""
O Filtro Personalizado (Juntando tudo)
No Python, existe uma função nativa chamada filter(), mas aqui nós vamos construir 
a nossa própria versão dela para entender como funciona por debaixo dos panos.

O que você deve fazer:

Crie uma função chamada eh_par(numero) que retorna True se o número for par, e False se for ímpar.

Crie uma função de alta ordem chamada filtrar_lista(lista, regra).

A filtrar_lista deve criar uma lista vazia, passar por cada item da lista original usando um for, 
e passar o item pela função regra. Se a regra retornar True, o item entra na lista nova.
"""

def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


def filtrar_lista(lista, regra):
    lista_nova = []
    for valor in lista:
        resultado = regra(valor)
        if resultado:
            lista_nova.append(valor)
    return lista_nova


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = filtrar_lista(numeros, eh_par)

print(pares)
