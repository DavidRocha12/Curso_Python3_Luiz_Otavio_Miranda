"""
Tipo Tupla - Uma lista imutável

Uma tupla é criada se caso a lista não for modificada, ela está sendo criada
apenas para depois mostrar os elementos dentro dela, e não ser modificada.

"""

tupla = "Maria", "Helena", "Luiz" # Assim é uma tupla
print(tupla)

tupla_2 = ("Maria", "Helena", "Luiz")# expecificando diretamente uma tupla
print(tupla_2)

lista = ["Maria", "Helena", "Luiz"]
tupla_3 = tuple(lista) # convertendo lista para tupla
print(tupla_3)
lista_2 = list(tupla_3)
print(lista_2)# convertendo tupla para lista

"""
Resultados:

('Maria', 'Helena', 'Luiz')
('Maria', 'Helena', 'Luiz')
('Maria', 'Helena', 'Luiz')
['Maria', 'Helena', 'Luiz']
"""