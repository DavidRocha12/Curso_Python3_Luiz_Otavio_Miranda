"""
split e join com list e str

split - divide uma string
join - une uma string
"""

frase = "Olha só que, coisa interessante"

lista_palavra = frase.split()# no split se não passar nenhum
# argumento nele, ele vai separar todas palavras em uma
# lista.

print(lista_palavra)

# Resultado:

# ['Olha', 'só', 'que,', 'coisa', 'interessante']

lista_frases = frase.split(",") # Aqui vai separar as plavras pela
# virgula, separando a linha em duas frase dentro de uma lista.
# veja o resultado abaixo:

print(lista_frases)

# Resultado:

# ['Olha só que', ' coisa interessante']

# .strip() tira espaços tando da direita ou esquerda da string,
# sendo espaços do inicio e fim da frase

# .rstrip() tira espaços da direita, sendo espaços 
# que estejam no inicio da frase.

# .lstrip() tira espaços da esquerda, espaços que 
# estejam no final da frase.

# utilizando o for em lista_frases:

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip())
    # Aqui está tirando o espaço no inicio e fim da frase

# resultado:

# Olha só que
# coisa interessante

# Unindo frases novamente utilizando .join:

frases_unidas = ",".join(lista_frases)
# no join é possível utilizar strings, tuplas ou listas,
# somente o que é iterável, se utilizar números inteiros, vai dar erro.

print(frases_unidas)

# resultado:

# Olha só que, coisa interessante

# Frase voltou a ser como estava no 
# inicio, porque juntei ela com uma "," virgula.
