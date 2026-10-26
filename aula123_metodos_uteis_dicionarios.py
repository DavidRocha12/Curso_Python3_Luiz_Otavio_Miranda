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

pessoa = {
    "nome" : "David",
    "sobrenome" : "Edison da Rocha"
}

# utilizando o len vai falar quantas chaves tem no dicionário
print(len(pessoa))

# keys é retornado somente as chaves:
print(pessoa.keys())

# Resposta:
# dict_keys(['nome', 'sobrenome'])

# values é retornado somente valores:
print(pessoa.values())

# Resposta:
# dict_values(['David', 'Edison da Rocha'])

# items retorna chaves e valores
print(pessoa.items())

# Resultados:
# dict_items([('nome', 'David'), ('sobrenome', 'Edison da Rocha')])

# para mostrar chaves e valores mostrando for:

for chave, valor in pessoa.items():
    print(chave, valor)

# adicionando chave e valor se caso não existir:

pessoa.setdefault("idade", 36)

print(pessoa)

# Resultado:

# {'nome': 'David', 'sobrenome': 'Edison da Rocha', 'idade': 36}
