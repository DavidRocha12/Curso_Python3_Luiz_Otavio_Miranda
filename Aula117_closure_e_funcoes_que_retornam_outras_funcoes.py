"""
Closures e funções que retornam outras funções:

Um Closure (ou "fechamento", em português) é um recurso da 
programação onde uma função interna "lembra" e tem acesso às variáveis 
da função externa onde foi criada, mesmo depois que a função externa já 
terminou de ser executada.
Para facilitar o entendimento, pense em uma analogia: imagine que a 
função interna está saindo de casa (a função externa) e leva uma mochila. 
Dentro dessa mochila, ela guarda algumas variáveis importantes que pegou 
na casa. Mesmo que a casa feche ou deixe de existir (a função externa 
acaba), a função interna continua com a mochila nas costas e pode usar 
essas variáveis quando for chamada no futuro.

Em Python, para que um Closure seja criado, três regras devem ser
atendidas obrigatoriamente:

Deve haver uma função aninhada (uma função definida dentro de outra).

A função interna deve usar um valor definido no escopo da função externa.

A função externa deve retornar a função interna (sem executá-la, ou seja,
sem os parênteses ()).
"""

# Este tipo de função é considerado um closure
def criar_saudacao(saudacao):
	def saudar(nome):
		return f"{saudacao}, {nome}"
	return saudar


falar_bom_dia = criar_saudacao("Bom dia")
falar_boa_noite = criar_saudacao("Boa noite")

# Utilizando funções dentro de funções utilizando listas. 
for nome in ["Maria", "Joana", "Luiz"]:
	print(falar_bom_dia(nome))
	print(falar_boa_noite(nome))



