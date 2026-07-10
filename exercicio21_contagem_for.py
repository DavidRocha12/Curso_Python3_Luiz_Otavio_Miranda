"""
Exercício 2: A Contagem Regressiva (Foco no range)

Desafio:
Imagine que você está programando o painel de lançamento de um foguete. 
Crie um programa usando for e range() que faça uma contagem regressiva 
começando do 10 e indo até o 1. Assim que o laço terminar, o programa deve imprimir "Decolar! 🚀".

Exemplo de saída esperada:

Plaintext
10
9
8
...
2
1
Decolar!

Dica: A função range() pode receber três informações: range(início, parada, passo). 
Para ir de trás para frente, pense em como o "passo" (o incremento) deve ser configurado 
(ele precisa ser negativo!). Lembre-se também que o número de parada do range é exclusivo, 
ou seja, ele para um número antes do que você colocar lá.
"""
print("Contagem Regressiva")

for n in range(10, 0, -1):
    print(n)

print("Decolar !")
