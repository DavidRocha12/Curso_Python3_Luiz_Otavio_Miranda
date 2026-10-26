# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa(shalow copy)
# get - obtem uma chave
# pop - apaga um item com a chave específicada (del)
# popitm- Apaga o último item adicionado
# update - atualiza um dicionário com outro
import copy

pessoa = {
    "nome" : "David",
    "sobrenome" : "Edison da Rocha"
}

# O dicionário também tem o método copy e também é um método mutável,
# mas utilizando o copy ele faz uma copia raza(shallow copy)

d1 = {
    "c1" : 1,
    "c2" : 2,
}

print(d1)

d2 = d1.copy()

print(d2)

d2["c1"] = 1000

print(d2)

# copia raza significa se tiver uma lista dentro do dicionário, no d2
# vai mostrar a mesma lista, se tentar modifica-la vai mudar o valor do d1 
# também.

d1 = {
    "c1" : 1,
    "c2" : 2,
    "l1" : [0, 1, 2]
}

print(d1)

d2 = d1.copy()

d2["l1"][1] = 9999

print(d1)
print(d2)

# Resultado:

# a lista foi modificada nas duas variáveis
# {'c1': 1, 'c2': 2, 'l1': [0, 9999, 2]}
# {'c1': 1, 'c2': 2, 'l1': [0, 9999, 2]}

# importando o método do python copy, é possivel fazer uma copia profunda
# realmente copiar e modificar somente a copia:


d1 = {
    "c1" : 1,
    "c2" : 2,
    "l1" : [0, 1, 2]
}

print(d1)

d2 = copy.deepcopy(d1)

d2["l1"][1] = 9999

print(d1)
print(d2)

# Resultado:
# {'c1': 1, 'c2': 2, 'l1': [0, 1, 2]}
# {'c1': 1, 'c2': 2, 'l1': [0, 9999, 2]}

# Aqui modificou somente a copia
