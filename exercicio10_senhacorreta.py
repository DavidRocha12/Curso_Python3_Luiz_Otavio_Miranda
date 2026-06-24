"""
1. O Validador de Senha Segura

Objetivo: Criar um sistema de login que força o usuário a digitar a senha correta, mas com um limite de tentativas.

Regras: * A senha correta é "Python123".

O usuário tem no máximo 3 tentativas.

Use uma variável booleana acesso_concedido inicializada como False.

O while deve continuar rodando enquanto o acesso não for concedido e o número de tentativas for menor que 3.

Se acertar, mude a booleana para True e exiba "Acesso Permitido". Se esgotar as tentativas, exiba "Conta Bloqueada".
"""

acesso_concedido = False
contagem_bloqueio = 0
senha_correta = "Python123"
while True:
    nome = input("Login: ")
    senha = input("Senha: ")

    if senha == senha_correta:
        print("Acesso permitido")
        acesso_concedido = True
    elif senha != senha_correta:
        print("Senha incorreta!")
        contagem_bloqueio += 1
        if contagem_bloqueio >= 3:
            print("Conta Bloqueada")
            break
        
    if acesso_concedido == True:
        break

"""Solução do gemini

senha_correta = "Python123"
tentativas = 0
acesso_concedido = False

while not acesso_concedido and tentativas < 3:
    senha_digitada = input("Digite a sua senha: ")
    tentativas += 1
    
    if senha_digitada == senha_correta:
        acesso_concedido = True
    else:
        print(f"Senha incorreta! Tentativas restantes: {3 - tentativas}")

# Condicional booleana fora do loop
if acesso_concedido:
    print("🔓 Acesso concedido. Bem-vindo!")
else:
    print("🔒 Conta bloqueada após 3 tentativas erradas.")

"""