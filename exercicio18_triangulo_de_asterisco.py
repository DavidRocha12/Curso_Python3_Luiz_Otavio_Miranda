"""
Exercício: O Triângulo de Asteriscos

Desafio:
Seu objetivo é criar um programa em Python que desenhe um triângulo retângulo na tela usando o caractere *.
A altura do triângulo deve ser de 5 linhas.

E, claro, a regra de ouro do nosso treinamento se mantém: você deve usar obrigatoriamente um laço while dentro
de outro laço while.

Exemplo de como a saída deve ficar na tela:

Plaintext
*
**
***
****
*****
Dicas para resolver:

Controle de Linhas e Colunas: * O while externo vai controlar em qual linha você está (da linha 1 até a linha 5).

O while interno vai controlar a quantidade de asteriscos que serão impressos naquela linha específica (as colunas).

A Lógica Principal: Repare no padrão do desenho. O número de asteriscos em uma linha é sempre igual ao número da própria
linha (ex: na linha 3, você imprime 3 asteriscos). O seu laço interno precisa usar essa lógica como limite.

O Segredo do print:

Por padrão, toda vez que você usa a função print(), o Python pula para a linha de baixo. Para imprimir os asteriscos lado 
a lado na mesma linha, você deve adicionar o parâmetro end="" dentro do print. Exemplo: print("*", end="").

Quando o laço interno terminar de desenhar todos os asteriscos daquela linha, você vai precisar dar um "pulo de linha" 
antes do laço externo recomeçar. Para isso, basta colocar um print() vazio solto dentro do laço externo.

Pode construir seu código e mandar aqui para avaliarmos!
"""

print("Triângulo retângulo")
print("=" * 20)

print()

asterisco = 0

while asterisco < 5:
    asterisco += 1
    triangulo = 0
    while triangulo < asterisco:
        triangulo += 1
        print("*", end="")
    print()
