"""
Retorno de valores das funções (return)
"""

variavel = print("Luiz")
print(variavel) # aqui vai dar None por motivo que essa variável 
# não é um valor

# Resultado

# Luiz
# None

# O print é uma função que exibe um valor na tela

# Agora se é necessário utilizar algum valor ao invés de mostrar o valor
# é necessário retornar o valor, para poder utiliza-lo.

def soma(x, y):
	print(x + y)

soma1 = soma(2, 2)
soma2 = soma(3, 3)

# print(soma1 + soma2)# aqui vai dar erro, por motivo que o retorno é None

def soma(x, y):
	return x + y

soma1 = soma(2, 2)
soma2 = soma(3, 3)

print(soma1 + soma2)

# retornar um valor vai ser possível utilizar os valores da função.

# é possível ter somente um return por função

