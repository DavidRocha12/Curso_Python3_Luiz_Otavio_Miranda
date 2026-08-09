"""
Operação ternária (condoicional de uma linha)
<valor> if <condição> else <outro valor>
"""

print("Valor" if True else "outro valor")

# Resultado
# Valor

condicao = 10 == 11

variavel = 'valor' if condicao else "outro valor"
print(variavel)

# Resultado:
# outro valor

digito = 9
novo_digito = digito if digito <= 9 else 0 # ou
# novo_digito = 0 if digito > 9 else digito
print(novo_digito)

# Resultado:
# 9
