"""
Como o for funciona por debaixo dos panos: 
(next, iter, iterável, iterador)

next - me entregue o proxímo valor
iter - me entregue o seu iterador
iterável - str, range, etc...
iterador - quem sabe entregar um valor por vez
"""
texto = iter("David") #.__iter__() função iter() faz a mesma coisa que o método __iter__()
# aqui ele vai guardar os iteráveis que são as strings, mas ele vai mostrar somente o endereço
# do objeto.
print(texto)
"""
resultado:

<str_ascii_iterator object at 0x785d979e26b0>
"""
# Para mostrar a iteração item por item é necessário chamar o método ou função next.

print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())

# print(texto.__next__()) se chamar esse ultimo print como o nome tem 5 letras ela vai iterar 5 vezes,
# se chamar novamente e não existir nada a mostrar vai gerar o erro StopIteration.

# E pode ser usado a função do next também:
texto = iter("David")

print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))

"""
resltado de ambos:

D
a
v
i
d

"""
texto = "Luiz" # Iterável
iterador = iter(texto) # Iterator

# Por debaixo dos panos praticamente é isso que o for faz:
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
"""
resposta:

L
u
i
z

"""
# Fazendo o for o procedimento fica simples:

for letra in texto:
    print(letra)
"""
Resultado:

L
u
i
z

"""
