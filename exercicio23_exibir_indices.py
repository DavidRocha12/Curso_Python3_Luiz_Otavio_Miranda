"""
Exibir os índices na lista de forma simples utilizando o range:

0 Maria
1 Luiz
2 João
"""

lista = ["Maria","Luiz", "João"]
indice = range(len(lista))
print(indice)
for i in indice:
    print(i, lista[i])

"""
resultado:

0 Maria
1 Luiz
2 João

Exercício utilizando o for e o range para mostrar o indice, 
mas existe um forma direta no pytho para mostrar indices. 
"""
