"""
Exercícios

Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro.
"""

# high-order funtion
def multiplicador(vezes_de_multiplicacao):
	def valor(numero):
		return numero * vezes_de_multiplicacao
	return valor
	


dobro = multiplicador(2)

print(dobro(5))

triplo = multiplicador(3)

print(triplo(5))

quadruplo = multiplicador(4)

print(quadruplo(5))

