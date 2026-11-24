"""
Atualização de Estoque

Você tem um dicionário representando o estoque atual de uma loja. 
Um caminhão de entregas acabou de chegar com novos produtos e reposições.

O que você deve fazer:
Escreva um código que passe pelos itens da entrega. Se o produto já existir no estoque, 
some a quantidade. Se o produto for novo, adicione ele ao estoque.
"""
estoque = {"Camiseta": 10, "Calça": 5, "Meia": 12}
entrega = {"Camiseta": 5, "Jaqueta": 4, "Meia": 3, "Boné": 2}

for chave, valor in entrega.items():
    if chave in estoque:
        estoque[chave] = estoque[chave] + valor
    else:
        estoque[chave] = valor

print(estoque)
