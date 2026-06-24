frase = "O Python é uma linguagem de programação "\
    "Multiparadigma. " \
    "Python foi criado por Guido van Rossun."

# Barra invertida vai quebrar a linha par digitar na linha abaixo 
# e não dar erro!

print(frase.count("Python"))
"""
acount vai verificar se a palavra existe dentro da frase
Se tiver maiuscula ou minuscula vai ter diferença, vai ser procurado
somente as palavras que sejam iguais as que você digitou.
Então, quando for verificar isso é melho fazer as palavras ficarem
    todas maiúsculas ou todas minúsculas com o .lower() ou .upper() 
"""

frase = "O Python é uma linguagem de programação "\
    "Multiparadigma. " \
    "Python foi criado por Guido van Rossun.".lower()

print(frase.count("python"))

frase = "O Python é uma linguagem de programação "\
    "Multiparadigma. " \
    "Python foi criado por Guido van Rossun.".upper()

print(frase.count("PYTHON"))

# Todos os resultados irão ser 2

i = 0
quantidade_vezes = 0
letra_mais_vezes = ""
while i < len(frase):
    letra_atual = frase[i]

    vezez_letras = frase.count(letra_atual)

    if letra_atual == " ":
        i += 1
        continue

    if quantidade_vezes < vezez_letras:
        quantidade_vezes = vezez_letras
        letra_mais_vezes = letra_atual
        
    i += 1


print(f"A letra que apareceu mais vezes é {letra_mais_vezes} que apareceu {quantidade_vezes} vezes")