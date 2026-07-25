"""
Enumerate para enumerar valores de iteráveis

Utilizando o enumerate, é possível numerar os elementos de sua lista,
os numeros inicia pelo 0 da mesma forma dos índices de cada item.
veja o exemplo abaixo:
"""

lista = ["Maria", "Helena", "Luiz"]
lista.append("João")# addicionando item na lista para mostrar que funciona normalmente.           

for indice, nome in enumerate(lista):
    print(indice, nome)

# Aqui vai mostrar o índice e o elemento da lista.
