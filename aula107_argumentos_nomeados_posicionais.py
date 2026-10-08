"""
Argumentos nomeados e argumentos posicionais(não nomeados)
em funções

Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado refcebe apenas o argumento (valor)
"""

def soma(x, y, z):
    # Definição da função
    # veja argumentos nomeados dentro da função:
    print(f'{x=} + y={y}', '|', 'x + y = ', x + y)

soma(1, 2, 3)

#recebendo argumentos nomeados na função:
soma(x=3, y=4, z=5)
soma(1, y=2, z=5) # Se foi colocado algun argumento nomeado, todos os proxímos
# argumentos tem que ser nomeados
