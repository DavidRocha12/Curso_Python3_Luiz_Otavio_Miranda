"""
Exercício: O Importador de Categorias

O Cenário:
Imagine que você vai permitir que o usuário cadastre vários "Tipos de Conta" de uma vez só, 
digitando tudo em uma única linha, separados por vírgula. O problema é que o usuário é descuidado: 
ele digita espaços a mais no começo, no meio e no fim.

O seu programa precisa pegar esse texto feio, separar as categorias, limpar a sujeira e depois 
mostrar na tela as categorias formatadas lindamente.

O Ponto de Partida:
Copie esse código para o seu arquivo:

Python

# O texto bagunçado digitado pelo usuário
entrada_usuario = "   Gastos essenciais, Bancos , Recebimentos  ,  Lazer,  Saúde   "

# Lista vazia que vai guardar as categorias limpas
categorias_limpas = []
As Regras do Sistema (Passo a Passo):

Cortar (split): Crie uma variável chamada lista_suja. Use o método .split(",") 
na entrada_usuario para transformar esse texto único em uma lista de várias categorias 
(cortando toda vez que houver uma vírgula).

Limpar (for + strip): Crie um laço for para percorrer cada item dentro da sua nova lista_suja.

Para cada item do laço, use o .strip() para remover os espaços em branco das pontas. 
Adicione esse item limpo dentro da lista categorias_limpas usando o .append().

Juntar (join): Agora que você tem uma lista perfeitamente limpa, crie uma variável chamada texto_final. 
Use o comando " | ".join(...) para juntar a sua lista categorias_limpas em um único texto novamente, 
mas agora separados por uma barra elegante.

O Relatório Final: Imprima o texto_final na tela.

Exemplo de como o console deve ficar no final:

Plaintext
Categorias cadastradas com sucesso:
Gastos essenciais | Bancos | Recebimentos | Lazer | Saúde
Pode montar o seu código e mandar aqui!
"""
entrada_usuario = "     Gastos essenciais , Bancos , Recebimentos , Lazer,  Saúde   "

categorias_limpas = []

lista_suja = entrada_usuario.split(",")

for item in lista_suja:
    item_limpo = item.strip()
    categorias_limpas.append(item_limpo)

print("Categoria cadastrada com sucesso: ")

texto_final = " | ".join(categorias_limpas)
print(texto_final)
