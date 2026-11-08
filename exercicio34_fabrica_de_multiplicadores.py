"""
Fábrica de Multiplicadores (Closure)

Aqui você vai criar uma função que fabrica outras funções. 
A função de dentro vai lembrar do valor que foi passado para a função de fora.

O que você deve fazer:

Crie uma função chamada criar_multiplicador(fator).

Dentro dela, crie outra função chamada multiplicar(numero).

A função de dentro deve retornar o numero multiplicado pelo fator (que veio da função de fora).

A função de fora deve retornar a função de dentro (sem os parênteses, para não executá-la!).
"""

def criar_multiplicador(fator):
    def multiplicar(numero):
        mult = fator * numero
        return mult
    return multiplicar


dobro = criar_multiplicador(2)
triplo = criar_multiplicador(3)

print(dobro(5))
print(triplo(5))
