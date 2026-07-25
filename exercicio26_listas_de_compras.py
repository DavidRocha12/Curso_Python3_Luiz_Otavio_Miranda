"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de inserir,
apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices
inexistentes na lista.
"""
import os

lista = []
while True:
    inserir = input("Selecione uma opção \n[i]nserir [a]pagar [l]istar [s]air: ").lower()
    os.system("clear")
    if len(inserir) > 1:
        print("Insira somentes uma letra!")
        continue
    
    if inserir not in "ials":
        print("Insira somente as letra inicias das opções.")
        continue

    if inserir == "l":
        if not lista:
            print("Lista Vazia")
            continue

        for i, nome in enumerate(lista):
            print(i, nome)
       
    elif inserir == "i":
        nome = input("Digite o que deseja inserir: ")
        lista.append(nome)

    elif inserir == "a":
        try:
           apagar = int(input("Insira o índice para apagar: "))
           lista.pop(apagar)
        
        except IndexError:
            print("Índice não existe!")
            continue
    elif inserir == "s":
        print("Saindo...")
        break