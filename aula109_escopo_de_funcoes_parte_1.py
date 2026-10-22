"""
Escopo de fuções em python

Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e o local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
"""

# exemplo de função sobre escopo:

def escopo():
	x = 1
	print(x)
	# a variável x não pode ser acessado fora da função
	# a variável vai estar protegido

# o código só vai ser executado se a função for chamada
escopo()

def escopo_2():
	x = 1
	breakpoint()
	def outra_funcao():
		y = 2
		print(x, y)
		breakpoint()
	# aqui eu consigo acessar o x, mas não consigo acessar o y da função
	# interna
	outra_funcao()
	breakpoint()
	print(x)


escopo_2()

"""
Tudo que está dentro da função, não é possível ser modificado
do lado de fora da função
"""

# se você querer manipula uma variável de dentro da função, é necessário
# colocar o comando global dentro da função, o valor da variável que está
# fora da função,vai ser o valor que estádentro da função, veja abaixo:

x = 1

def escopo_3():
	global x # aqui vai poder acessar a variável fora da função, e 
	# transforma-la com o valor da variavel x interna.
	x = 10

	def outra_funcao():
		x = 11
		y = 2
		print(x, y)# Variável x dentro da outra função

	outra_funcao()
	print(x)# variável x dentro da função

escopo_3()
print(x)
