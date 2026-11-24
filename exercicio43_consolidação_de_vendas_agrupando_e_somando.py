"""
Consolidação de Vendas (Agrupando e Somando)

Você tem uma lista de transações de uma empresa. Cada transação é 
um dicionário com o nome do vendedor e o valor da venda. Um mesmo 
vendedor aparece várias vezes.

O que você deve fazer:

Crie um dicionário chamado total_por_vendedor que some o valor 
total vendido por cada pessoa.

"""

vendas = [
    {"vendedor": "Carlos", "valor": 500.0},
    {"vendedor": "Ana", "valor": 1200.0},
    {"vendedor": "Carlos", "valor": 300.0},
    {"vendedor": "Bia", "valor": 850.0},
    {"vendedor": "Ana", "valor": 450.0}
]

total_por_vendedor = {}


for vendedores in vendas:
    nome = vendedores["vendedor"]
    valor = vendedores["valor"]

    if nome in total_por_vendedor:
        total_por_vendedor[nome] += valor
    else:
        total_por_vendedor[nome] = valor
        
print(total_por_vendedor)

# Resultado esperado:
# {'Carlos': 800.0, 'Ana': 1650.0, 'Bia': 850.0}