# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa(shalow copy)
# get - obtem uma chave
# pop - apaga um item com a chave específicada (del)
# popitem- Apaga o último item adicionado
# update - atualiza um dicionário com outro

p1 = {
    "nome" : "David",
    "sobrenome" : "Rocha"
}

# Ao invés dos [] posso utilizar o get para visualizar
# os dados das variáveis.

print(p1["nome"])
print(p1.get("nome"))

# utilizando pop para apagar itens do dicionário pela chave especificada:

# nome = p1.pop("nome")
# print(nome)
# print(p1)
# Acima vai mostrar que a chave nome e o objeto dele foi apagado

# popitem apaga o ultima chave do dicionário:

ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)

# update atualiza seu dicionário ou adiciona chaves no dicionário, update 
# pode receber listas e tuplas também veja o exemplo abaixo:

p1.update(nome="novo valor", idade=30)
print(p1)

# tupla = (("nome", "novo valor"), ("idade", 30))
# lista = [["nome", "novo valor"]], ["idade", 30]]
