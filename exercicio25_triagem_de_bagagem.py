"""
Exercício: A Triagem de Bagagens no Aeroporto

O Cenário:

Você é o programador responsável pela esteira de um aeroporto. As bagagens passam por 
um sensor que registra o peso delas em uma lista. O seu programa precisa ler essa lista, 
separar as malas aceitas das malas com excesso de peso, bloquear malas perigosamente pesadas e, 
por fim, fazer alguns ajustes de última hora.

O Ponto de Partida:
Copie as variáveis abaixo para o início do seu código:

Python
pesos_esteira = [12, 25, 32, 18, 24, 40, 15, 22]
voo_regular = []
voo_excesso = []
malas_atrasadas = [10, 14]
As Regras do Sistema (Passo a Passo):

A Varredura: Use um laço for para percorrer cada peso dentro da lista pesos_esteira.

Triagem (if/elif/else e append):

Se o peso for menor ou igual a 23, adicione esse peso à lista voo_regular.

Se o peso for entre 24 e 30 (inclusive), adicione à lista voo_excesso.

Se o peso for maior que 30, imprima a mensagem "ALERTA: Bagagem de [PESO] kg bloqueada por 
limite de segurança!" e use o comando continue para pular para a próxima mala sem adicioná-la a lugar nenhum.

Ajuste VIP (pop ou del): Após o término do laço for, o sistema descobre que a primeira mala que entrou na lista 
voo_regular pertence ao piloto e deve ir para a cabine. Remova-a da lista voo_regular (índice 0).

Os Atrasados (extend): Duas malas chegaram atrasadas (lista malas_atrasadas). Adicione o conteúdo 
dessa lista ao final da lista voo_regular.

O Relatório Final: Imprima na tela como ficaram as listas voo_regular 
e voo_excesso no final de todo o processo.

Exemplo de como o console deve ficar no final:

Plaintext
ALERTA: Bagagem de 32 kg bloqueada por limite de segurança!
ALERTA: Bagagem de 40 kg bloqueada por limite de segurança!

Lista do Voo Regular: [18, 15, 22, 10, 14]
Lista com Excesso: [25, 24]
(Repare que o número 12, que era o primeiro da lista regular, 
sumiu porque foi entregue ao piloto no Passo 3).
"""

pesos_da_esteira = [12, 25, 32, 18, 24, 40, 15, 22]
voo_regular = []
voo_excesso = []
malas_atrasadas = [10, 14]

for peso in pesos_da_esteira:
    if peso <= 23:
        voo_regular.append(peso)
    elif peso >= 24 and peso <= 30:
        voo_excesso.append(peso)
    elif peso > 30:
        print(f"ALERTA: Bagagem de {peso} kg bloqueada por limite de segurança!")
        continue

del voo_regular[0]

voo_regular.extend(malas_atrasadas)

print()
print(f"Lista do Voo Regular: {voo_regular}")
print(f"Lista com Excesso: {voo_excesso}")
