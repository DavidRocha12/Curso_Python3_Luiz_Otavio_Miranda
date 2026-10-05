"""
Cálculo do primeiro digito:

CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando de 10

Ex.: 746.824.890-70 (746824890)
 *  10 9  8  7  6  5  4  3  2
    7  4  6  8  2  4  8  9  0
    70 36 48 56 12 20 32 27 0 
    
Somar todos os resultados:

70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301

Multiplicar o resultado anterior por 10

301 * 10 = 3010

obter o resto da divisão da conta anterior por 11

3010 % 11 = 7

se o resultado anterior for maior que 9:

    o resultado é 0

contrário disso:

    o resultado é o valor da conta

O primeiro  digito do CPF é 7
"""

cpf = "746.824.890-70"

lista = cpf.split(".")

juntar_numeros = "".join(lista)

separar_nove_numeros = juntar_numeros.split("-")

juntar_tudo = "".join(separar_nove_numeros)

print(juntar_tudo)

junto = juntar_tudo[:9]
cont = 10
soma = 0
for item in junto:
    mult = int(item) * cont
    print(cont)
    cont -= 1
    soma += mult

mult_1 = soma * 10

primeiro_digito = mult_1 % 11

print(f"O primeiro Digito do CPF é {primeiro_digito if primeiro_digito <= 9 else 0}")