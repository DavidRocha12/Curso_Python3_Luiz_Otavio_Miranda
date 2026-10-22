"""
args - Argumentos não nomeados

* - *args (empacotamneto e desempacotamento)
"""

x, y, *resto = 1, 2, 3, 4 # x e y está desempacotando, e o *resto está empacotando
print(x, y, resto)

# Resultado

#1 2 [3, 4]

# Quando é necessário criar uma função que é necessário receber vários 
# argumentos, é necessário colocar *args, é possível colocar outros nomes
# ao invés de args, sim, é possível, mas por convenção dos programadores
# em python, tem que colocar *args.

# Veja uma função de soma que pode receber vários parametros:

def soma(*args)
	total = 0
	for numero in args:
		print("Total", total, numero)
		total = total + numero
	print(total)


soma(1, 2, 3, 4, 5, 6)
