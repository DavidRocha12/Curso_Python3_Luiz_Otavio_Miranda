"""
Exercício

Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
    """

#Seu nome é {nome}
#Seu nome invertido é {nome invertido}
#Seu nome tem {n} letras
#A primeira letra do nome é {letra}
#A ultima letra do nome é {letra}

#Se nada for digitado em nome ou idade:
#    Exiba "Desculpe, você deixou campos vazios."

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print()

if nome and idade:
    
    nome_invertido = nome[::-1]
    n = len(nome)
    letra = nome[0]
    letras = nome[-1]

    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome_invertido}")

    if " " in nome:
        print("Seu nome contém espaços.")
    else:
        print("Seu nome não contém espaços")
        
    print(f"Seu nome tem {n} letras.")
    print(f"A primeira letra do nome é {letra}")
    print(f"A última letra do seu nome é {letras}")
else:
    print("Desculpe, você deixou campos vazios.")
