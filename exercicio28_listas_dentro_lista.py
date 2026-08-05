"""
Exercício: Calculando o Saldo do Extrato

O Cenário:

O seu sistema registrou várias movimentações durante o mês. 
Elas foram salvas em uma lista principal chamada extrato. Cada item 
dentro desse extrato é outra lista contendo três informações: 

[Tipo, Descrição, Valor].

Seu objetivo é navegar por essas listas internas, extrair os valores corretos 
e calcular se o usuário terminou o mês no azul ou no vermelho.

O Ponto de Partida:
Copie este código para o seu arquivo:

Python
# Lista principal contendo listas menores (Tabela de transações)
extrato = [
    ["Receita", "Salário", 2500.00],
    ["Despesa", "Mercado", 450.00],
    ["Receita", "Venda de Livro", 80.00],
    ["Despesa", "Internet", 120.00]
]

saldo_final = 0
As Regras do Sistema (Passo a Passo):

Acessando um dado específico: Antes de calcular tudo, o programa precisa mostrar 
qual foi o valor gasto no Mercado. Sem usar laços, use o sistema de duplo índice 
(ex: lista[linha][coluna]) para imprimir apenas o número 450.00.

A Varredura: Crie um laço for para percorrer a lista extrato.
(Dica: A cada giro do laço, a sua variável temporária será uma lista inteira com 3 itens).

O Cálculo: Dentro do laço, crie um if/else:

Se o item da posição 0 for igual a "Receita", some o valor (posição 2) à variável saldo_final.

Se o item da posição 0 for igual a "Despesa", subtraia o valor da variável saldo_final.

O Relatório Final: Fora do laço for, imprima o saldo_final na tela.

Exemplo de como o console deve ficar no final:

Plaintext
O valor gasto no mercado foi: R$ 450.0
Saldo final do mês: R$ 2010.0

Pode montar o seu código e mandar aqui quando terminar. Preste atenção nos índices: 
o primeiro item de uma lista sempre é o 0!
"""

extrato = [
    ["Receita", "Salário", 2500.00],
    ["Despesa", "Mercado", 450.00],
    ["Receita", "Venda de Livro", 80.00],
    ["Despesa", "Internet", 120.00]
]

print(f"Valor gasto no mercado R$ {extrato[1][2]:.2f}")

saldo_final = 0
for lista in extrato:
    print(lista)
    if lista[0] == "Receita":
        saldo_final += lista[2]
    else:
        saldo_final -= lista[2]

print(f"Saldo_Final: R$ {saldo_final:.2f}")
