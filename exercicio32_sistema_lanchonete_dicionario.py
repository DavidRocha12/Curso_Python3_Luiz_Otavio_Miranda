"""
Sistema de Lanchonete (Somando Valores)

Neste cenário, você tem um cardápio. O usuário vai escolher um item pelo número dele (assim como no seu quiz),
mas em vez de dizer se ele acertou ou errou, você deve mostrar o nome do produto escolhido e adicionar o valor
dele a uma "conta".

O que você deve fazer:

Mostre o cardápio numerado. Peça para o usuário escolher o número de um lanche e o número de uma bebida. 
No final, mostre o que ele comprou e o valor total da conta. Use o try/except para evitar que o código 
quebre se ele digitar uma letra.
"""

cardapio = [
    {"Item": "Hamburguer", "Preco": 25.50},
    {"Item": "Batata Frita", "Preco": 12.00},
    {"Item": "Refrigerante", "Preco": 8.00},
    {"Item": "Suco Natural", "Preco": 10.00}
]

print("--- CARDÁPIO ---")

for indice, item in enumerate(cardapio):
    print(f"{indice}) {item["Item"]} - R$ {item["Preco"]:.2f}")

print()
try:
    soma = 0

    escolha_lanche = int(input("Escolha número do lanche: "))
    escolha_bebida = int(input("Escolha o número da bebida: "))

    pedido = len(cardapio)

    print()

    if escolha_lanche <= pedido and escolha_bebida < pedido :
        print("Pedido Concluído!")
        print(f"Itens: {cardapio[escolha_lanche]["Item"]} e {cardapio[escolha_bebida]["Item"]}")

        soma = cardapio[escolha_lanche]["Preco"] + cardapio[escolha_bebida]["Preco"]

        print(f"Total a pagar: R$ {soma:.2f}")
    else:
        print("Esse item não existe no cardápio!")

except ValueError:
    print("Erro! Você não digitou um número válido. Pedido Cancelado.")