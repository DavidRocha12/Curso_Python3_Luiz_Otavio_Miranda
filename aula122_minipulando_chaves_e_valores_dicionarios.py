# Manipulando chaves e valores em dicionários

pessoa = {}

# criando chaves
pessoa["nome"] = "David"

print(pessoa)

# Resultado:

# {'nome': 'David'}

# se tentar acessar uma chave que não existe vai dar erro:
# print(pessoa["nome_1"])
# vai dar erro: keyerror

# criando outra chave
pessoa["sobrenome"] = "Edison da Rocha"

print(pessoa)
# Resultado

# 'nome': 'David', 'sobrenome': 'Edison da Rocha'}

# apagando chave
del pessoa["sobrenome"]
print(pessoa)

# Resultado
# {'nome': 'David'}

# Para verificar se chave existe ou não é possível utilizar o metodo .get ou 
# utilizar o try/execept para não dar erro:

print(pessoa.get("sobrenome"))
# Resultado:
# None

# O método .get se não existir o que ele está verificando, ele retorna None
if pessoa.get("sobrenome") is None:
    print("Não existe")
else:
    print(pessoa["sobrenome"])

