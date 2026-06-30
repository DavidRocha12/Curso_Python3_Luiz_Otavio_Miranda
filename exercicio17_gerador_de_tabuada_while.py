"""
Exercício: O Gerador de Tabuadas (while aninhado)
Desafio:
Escreva um programa em Python que imprima as tabuadas de multiplicação do 1 ao 5. Para cada um desses números,
 o programa deve mostrar a multiplicação de 1 a 10.

A regra de ouro aqui é: você não pode usar o laço for. A solução deve ser construída obrigatoriamente usando 
um laço while dentro de outro laço while.

Exemplo de como a saída deve ficar na tela (resumida):

Plaintext
Tabuada do 1:
1 x 1 = 1
1 x 2 = 2
...
1 x 10 = 10

Tabuada do 2:
2 x 1 = 2
...
Dicas para resolver:

Variáveis de controle: Você vai precisar de duas variáveis contadoras (por exemplo, i para o número da 
tabuada atual e j para o multiplicador de 1 a 10).

O while externo: Vai controlar de qual número é a tabuada atual (de 1 até 5).

O while interno: Vai fazer a contagem de 1 a 10 para realizar as multiplicações do número atual.

Atenção ao reset: Não se esqueça de zerar (ou voltar para 1) a variável de controle do while interno toda vez que o
while externo recomeçar um ciclo, senão a segunda tabuada não vai imprimir nada!

Pode tentar montar o código e jogar aqui para eu dar uma olhada. Se o código travar em um loop infinito, não se preocupe,
faz parte do aprendizado com o while!
"""