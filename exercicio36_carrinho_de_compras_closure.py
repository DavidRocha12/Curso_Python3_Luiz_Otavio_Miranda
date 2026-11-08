"""
O Carrinho de Compras (Closure com Memória)

No desafio do multiplicador, a função interna lembrava de um número. 
Agora, ela vai lembrar de uma lista.

O que você deve fazer:

Crie uma função criar_carrinho(). Dentro dela, crie uma lista vazia chamada itens = [].

Crie uma função interna chamada adicionar(produto).

A função interna deve adicionar o produto na lista itens e retornar a lista completa.

Retorne a função interna (sem executá-la).
"""

def criar_carrinho():
    itens = []
    def adicionar(produto):
        itens.append(produto)
        return itens
    return adicionar

    
meu_carrinho = criar_carrinho()
print(meu_carrinho("Maçã"))
print(meu_carrinho("Banana"))
print(meu_carrinho("Uva"))
