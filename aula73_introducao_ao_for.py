"""
Introdução ao for / in - Estrutura de repetição para coisas finitas

O for é utilizado para fazer códigos de repetição que é possível saber quantas vezes 
ele vai ser executado, essa estrutura de repetição tem limites definidos, diferente do while, 
que enquanto não colocar o comando de parada, ele continua executando.

O código abaixo mostra a iteração de strings utilizando for:
"""

texto = "Python"

texto_novo = ""
for letra in texto:
    texto_novo += f"*{letra}"
    print(letra)
print(texto_novo + "*")

"""
Resultado:

P
y
t
h
o
n
*P*y*t*h*o*n*
"""
