"""
Filtro de Estoque por Categoria

Você recebeu o catálogo de uma loja de eletrônicos onde cada produto
tem um preço, uma categoria e uma quantidade em estoque.

O que você deve fazer:

Crie um dicionário novo chamado perifericos_disponiveis. 
Ele deve conter apenas o nome do produto e o preço dos itens 
que sejam da categoria "Perifericos" e que tenham estoque maior 
que zero.
"""

catalogo = {
    "Mouse Gamer": {"categoria": "Perifericos", "preco": 150.0, "estoque": 12},
    "Monitor 24": {"categoria": "Monitores", "preco": 850.0, "estoque": 5},
    "Teclado Mecânico": {"categoria": "Perifericos", "preco": 320.0, "estoque": 0},
    "Headset": {"categoria": "Perifericos", "preco": 210.0, "estoque": 4},
    "Cadeira Gamer": {"categoria": "Moveis", "preco": 1100.0, "estoque": 2}
}

perifericos_disponiveis = {}

for nome, valor in catalogo.items():
    if valor["categoria"] == "Perifericos" and valor["estoque"] > 0:
        perifericos_disponiveis[nome] = valor["preco"]


print(perifericos_disponiveis)
    

# Seu código começa aqui...

# Resultado esperado:
# {'Mouse Gamer': 150.0, 'Headset': 210.0}
