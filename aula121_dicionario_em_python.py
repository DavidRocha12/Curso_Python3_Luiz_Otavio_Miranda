"""
Dicionário em Python(tipo dict)

Dicionários são estruturas de dados do tipo par de "chave" e "valor"
Chaves podem ser considradas como "índices" que vimos na lista e podem ser
de tipos imutáveis como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos as chaves - {} ou a classe dict para criar dicionários.
Imutáveis: str, int, float, bool, tuple
Mutáveis: dict, list
"""

# Criando dicionário

pessoa = {
	"nome" : "David",
	"sobrenome" : "Rocha",
	"idade" : 36,
	"altura" : 1.72,
	"endereço" : [
	{"rua" : "nome", "número" : 20},
	{"rua" : "trabalho", "número" : 50}
	]
}

print(pessoa, type(pessoa))

# acessando itens expecíficos do dicionário:
print(pessoa["nome"])
print(pessoa["sobrenome"])

for chave in pessoa:
	print(chave, pessoa[chave])

