"""
Introdção ao Empacotamento e Desempacotamento
"""

lista = ["Maria", "Helena", "Luiz"]# Em lista os elementos que estão dentro dela estão empacotados dentro dela, 
# e é possível fazer o desempacotamento dela. Todo elemento iterável é possível fazer o desempacotamento dele.

# Para desempacotar um  iteráve, é necessário criar variáveis para valores desempacotados e criar uma variável 
# para empacotar o restante se caso a lista for grande.
# Veja o exemplo abaixo mostrando o desempacotamento de um nome e o empacotamento do restante:

nome, nome2, nome3 = lista # Se caso a lista for pequena
print(nome)
print(nome2)
print(nome3)

# Fazendo lista diretamente com as variáveis:
nome, nome2, nome3 = ["Maria", "Helena", "Luiz"]

print(nome, nome2, nome3)

# Desempacotando 1 elemento e empacotando o restante:
nome, *resto = ["Maria", "Helena", "Luiz"]
print(nome2)
print(resto)

# desempacotamento seguindo a convenção do programadores, se não for utilizar o restantes do itens empacotados:

nome, *_ = ["Maria", "Helena", "Luiz"]
print(nome, _)

# pegando o segundo elemento da lista:

_, nome2, *_ = ["Maria", "Helena", "Luiz"]
print(nome2, _) # Aqui vai mostrar o que está empacotado é apenas o Luiz, a 1° variável vai ser ignorada, 
# isso serve para pegar o elemento que deseja.

_, _, nome3, *_ = ["Maria", "Helena", "Luiz"]
print(nome3, _)# Vai mostrar Luiz, e a variável de empacotamento vai estar com a lista vazia.

"""
Resultados:

Maria
Helena
Luiz

Maria Helena Luiz

Helena
['Helena', 'Luiz']

Maria ['Helena', 'Luiz']

Helena ['Luiz']

Luiz []
"""

