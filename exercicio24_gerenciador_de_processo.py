"""
O Gerenciador de Processos
Desafio:
Você está construindo o núcleo de um sistema operacional simples. 
Escreva um código que siga os 7 passos abaixo na ordem exata.

Dica de ouro: Após cada passo, coloque um print(processos) para visualizar 
como a sua lista está sendo modificada em tempo real.

Passo a passo:

Surgimento (range): Crie uma lista chamada processos contendo os números de 1 a 5. 
Use a função list(range(...)) para gerar esses números sem precisar digitá-los um a um.

Nova tarefa (append): O sistema detectou uma nova operação. Adicione o processo número 6 
ao final da lista.

Prioridade Máxima (insert): Um processo crítico (número 99) precisa rodar imediatamente. 
Insira-o na primeira posição da fila (índice 0).

Sobrecarga (extend ou +): O sistema recebeu um pacote extra de tarefas. Crie uma nova lista chamada 
extras = [10, 11] e junte os elementos dela à sua lista principal processos.

Conclusão (pop): O último processo da fila concluiu seu trabalho. Remova-o da lista. 
Salve o valor removido em uma variável e imprima uma mensagem na tela: "Processo [X] concluído!".

Falha Crítica (del): O processo que agora ocupa o índice 2 travou. Apague-o da lista usando o comando del.

Reinicialização (clear): Fim do expediente. O sistema vai desligar. Esvazie a lista inteira para 
liberar a memória. Imprima a lista pela última vez para garantir que ela está vazia.

Exemplo do que deve aparecer no seu console:
(Não precisa fazer os textos bonitinhos de passo, apenas focar em imprimir a lista mudando)

Plaintext
Passo 1: [1, 2, 3, 4, 5]
Passo 2: [1, 2, 3, 4, 5, 6]
Passo 3: [99, 1, 2, 3, 4, 5, 6]
Passo 4: [99, 1, 2, 3, 4, 5, 6, 10, 11]
Processo 11 concluído!
Passo 5: [99, 1, 2, 3, 4, 5, 6, 10]
Passo 6: [99, 1, 3, 4, 5, 6, 10]
Passo 7: []
"""

print("Gerenciador de Processos")
processos = []
extra = [10, 11]

for n in range(1, 6):
    processos.append(n)

print(processos)

processos.append(6)

print(processos)

processos.insert(0, 99)

print(processos)

processos.extend(extra)

print(processos)

remover = processos.pop()

print(f"Processo {remover} concluido!")

print(processos)

del processos[2]

print(processos)

processos.clear()

print(processos)
