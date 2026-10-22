"""
Exercícios com funções

Crie uma função que multiplica todos os argumentos não nomeados rcebidos.
Retorne o total para uma variável e mostre o valor da variável.

Crie uma função que mostra se o número é par o impar
Retorne se o número é Par ou Impar.
"""

print(1*2*3*4*5)

def mult(*args):
	multi = 1
	for n in args:
		multi *= n
	return multi

valor = mult(1, 2, 3, 4, 5)

print(valor)

def par_ou_impar(numero):
	if numero % 2 == 0:
		return f"O valor {numero} é Par"
	else:
		re

valores = par_ou_impar(260)
 
print(valores)

# Resposta:

# 120
# 120
# O valor 260 é Par

