"""
Valores padrão para parâmetros

Ao definir uma função, os parâmetros podem 
ter valores padrão. Caso o valor não seja enviado para
o parâmetro, o valor padrão será usado.

Refatorar: Editar o seu código.
"""
# Se você for editar uma função, adicionar um novo parâmetro,
# é necessário colocar ele recebendo um valor 0 por exemplo,
# mas 0 é considerado um valor falsy, e se for utilizar o 0 no parâmetro
# o seu código vai entender que se é 0 não precisa ser usado, para não ter
# esse problema é melhor utilizar o parâmetro nomeado None, veja o exemplo abaixo:

# Função original:
def soma(x, y):
    print(x + y)


# Função refatorada, recebendo parâmetro nomeado z=0:
def soma(x, y, z=0):
    # verificando se existe parâmetro z, se é maior que 0
    if z:
        print(f"{x=}, {y=} {z=}", x + y + z)
    else:
        print(f"{x=} {y=}", x + y)


soma(1, 2)
soma(7, 9, 0)

# Resultado:

# x=1 y=2 3
# x=7 y=9 16

# O segundo resultado não apareceu o z, por motivo que ele considerou o valor
# 0 passado no parâmetro como falsy, executando o else, para resolver
# isso é necessário utilizar o parâmetro nomeado None.

def soma(x, y, z=None):
    if z is not None:
        print(f"{x=} {y=} {z=}", x + y + z)
    else:
        print(f"{x=} {y=}", x + y)

soma(100, 200)
soma(7, 9, 0)

# Resultado:

# x=100 y=200 300
# x=7 y=9 z=0 16

# O resultado acima está mostrando que o z resebeu o valor 0, 
# utilizando o parâmetro None, ele não ignorou o 0.
# O parâmetro None deve ser usado em certas ocasiões,
# se por exemplo utilizar None também no y e não tiver valor,e se
# a condição de decisão if/else não estive expecificando vai dar erro de 
# NoneType.

def soma(x, z=None, y=None):
    if z is not None:
        print(f"{x=} {y=} {z=}", x + y + z)
    else:
        print(f"{x=} {y=}", x + y)

soma(3, 5)

# Resultado:
"""
 File "/home/davidrocha/Meus Estudos/Curso_Python3_Luiz_Otavio_Miranda-main/aula108_valores_padrao_para_parametros_em_funcoes.py", line 65, in soma
    print(f"{x=} {y=} {z=}", x + y + z)
                             ~~^~~
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
"""
