"""
Imprecisão de ponto flutuante
"""

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)

"""
resultado:

 0.7999999999999999

 o resultado não vai ser redondo se calcular desta forma, 
 vai mostrar números quebrados.
 Para resolver isso é possível utilizar a formatação de strings, 
 uma função em python chamado round, ou o módulo decimal utilizando 
 o método decimal.

 veja abaixo os exemplos: 
"""

print(f"{numero_3:.2f}")
print(round(numero_3, 2))

import decimal # esse módulo é utilizado 
# se caso necessitar de um número preciso

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2

print(numero_3)

# Mas praticamente o modo que é utilizado o float utilizando a formatação
# resolve praticamente tudo. Os outros métodos são utilizados se forem realmente
# necessário.
