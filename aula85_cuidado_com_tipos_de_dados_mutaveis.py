"""
Cuidado com dados mutáveis
= - copiado o valor (Imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

nome = "David"
outro_nome = nome
nome = "Luiz"
print(nome)# Aqui o valor é imutável, mas se você apontar
# outro item para essa variável, este ultimo item é o que
# vai estar no lugar, ele sobreescreve o item na variável
# Para utiçizar o valor acima é necessário utilizar outra
# variável guarda o valor na memória
print(outro_nome)

# resultado:

# Luiz
# David

"""
# Abaixo existe uma lista e uma variável copiando essa lista,
mas se você modificar algo na primeira lista, na variável
que foi copiado a lista vai ser modificada também,
porque esta variável não está com uma cópia independente
e sim com a própria lista, o id delas são as mesmas na memória.
"""

lista_a = ["Luiz", "Maria"]
lista_b = lista_a.copy()# aqui voCê está coopiando a lista para outra váriável, assim ela vai estr em outro endereço na memória.
lista_a[0] = "David"
print(lista_a)
print(lista_b)

#Resultado:
# ['David', 'Maria'] a modificação foi feita na lista a

# Resultado utilizando copy:

# ['David', 'Maria']
# ['Luiz', 'Maria']
