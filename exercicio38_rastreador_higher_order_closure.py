"""
O Rastreador (Higher Order + Closure)

Este é o desafio mais avançado. Você vai criar uma função que recebe uma função, 
e retorna uma nova função que avisa quando está sendo executada. 
(Isso é exatamente o que um "Decorator" faz no Python!).

O que você deve fazer:

Crie uma função chamada rastreador(funcao).

Dentro dela, crie uma função envelope(texto).

A função envelope deve imprimir a frase "Atenção: executando a função agora!" e, 
na linha de baixo, retornar a execução da funcao(texto).

Retorne a função envelope.

Fornecerei a função gritar(palavra) pronta para você testar.
"""

def rastreador(funcao):
    def envelope(texto):
        print("Atenção: executando a função agora!")
        return funcao(texto)
    return envelope


def gritar(palavra):
    return palavra.upper() + "!!!"


gritar_rastreado = rastreador(gritar)
print(gritar_rastreado("Olá"))

@rastreador
def gritar(palavra):
    return palavra.upper() + "!!!"


print(gritar("Olá"))
