"""
Listas dentro de listas, pode ser tuplas também! 
"""

salas = [
    ["Maria", "Helena", ],
    ["Elaine", ],
    ["Luiz", "João", "Eduarda", (0, 10, 20, 30, 40)]
]

print(salas[1][0])

# resultado:

# Elaine

print(salas[0][1])

# Resltado:

# Helena

print(salas[2][2])

# Resultado

# Eduarda

print(salas[2][3][2])

# Resultado

# 20

# É possível mostrar com for:

for sala in salas:
    for item in sala:
        print(item)

# Resultado:

"""
Maria
Helena
Elaine
Luiz
João
Eduarda
(0, 10, 20, 30, 40)
"""

# Nessa aula está mostrando como você pode acessar 
# itens em listas ou tuplas diiretamente ou utilizando 
# o for, e que você pode ter dados mutáveis com imutáveis, 
# e iteráveis dentro de iteráveis.
