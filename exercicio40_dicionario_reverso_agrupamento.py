"""
O Dicionário Reverso (Agrupamento)

Você tem um dicionário onde a chave é o nome de um 
funcionário e o valor é o setor onde ele trabalha. 
Você precisa criar um relatório invertido: um dicionário onde 
a chave é o Setor, e o valor é uma lista com os nomes das pessoas 
daquele setor.

Dica: Lembre-se do método .items() para passear pelas chaves 
e valores ao mesmo tempo. Você precisará checar se o setor já 
existe no novo dicionário antes de fazer o .append().
"""

funcionarios = {
    "Ana": "TI",
    "Carlos": "RH",
    "Bia": "TI",
    "Daniel": "Vendas",
    "Eduardo": "Vendas",
    "Fernanda": "TI"
}

relatorio_setores = {}
for func, setor in funcionarios.items():
    if setor not in relatorio_setores:
        relatorio_setores[setor] = []
    relatorio_setores[setor].append(func)
    
print(relatorio_setores)

# O resultado esperado é: 
# {'TI': ['Ana', 'Bia', 'Fernanda'], 'RH': ['Carlos'], 'Vendas': ['Daniel', 'Eduardo']}