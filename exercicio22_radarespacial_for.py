"""
Exercício: O Radar Espacial
Desafio:
Você está programando o radar de uma nave espacial que precisa escanear os setores de voo 
do número 1 ao 12 em busca de rotas seguras. Crie um programa usando o laço for com range() 
para percorrer esses setores e aplique as seguintes regras usando if, elif e else:

Zona de Tempestade (continue): Se o radar estiver avaliando os setores 4 ou 9, o sistema deve 
imprimir "Setor [X]: Tempestade solar detectada. Pulando..." e pular imediatamente para o próximo 
setor, sem executar mais nada naquele ciclo.

Perigo Extremo (break): Se o radar chegar no setor 11, ele encontrou um buraco negro. O programa 
deve imprimir "Setor 11: BURACO NEGRO DETECTADO! Abortando varredura..." e parar o laço completamente.

Setor Seguro (else): Para todos os outros números, o radar deve imprimir "Setor [X]: Escaneado e seguro".

Exemplo de saída esperada no console:

Plaintext
Iniciando varredura do radar...
Setor 1: Escaneado e seguro
Setor 2: Escaneado e seguro
Setor 3: Escaneado e seguro
Setor 4: Tempestade solar detectada. Pulando...
Setor 5: Escaneado e seguro
Setor 6: Escaneado e seguro
Setor 7: Escaneado e seguro
Setor 8: Escaneado e seguro
Setor 9: Tempestade solar detectada. Pulando...
Setor 10: Escaneado e seguro
Setor 11: BURACO NEGRO DETECTADO! Abortando varredura...
Varredura encerrada.
Dicas para resolver:

Use o range(1, 13) para garantir que o radar avalie até o número 12.

Você pode usar o operador lógico or no seu if para verificar os setores 4 e 9 
em uma única condição (ex: if setor == 4 or setor == 9:).

As instruções continue e break devem ficar dentro dos seus respectivos blocos 
condicionais, logo abaixo do print de aviso.
"""
print("Radar Espacial")

print()

for nave in range(1, 13):
    if nave == 4 or nave == 9:
        print(f"Setor {nave}: Tempestade solar detectada. Pulando...")
        continue
    elif nave == 11:
        print(f"Setor {nave}: BURACO NEGRO DETECTADO! Abortando varredura...")
        break
    else:
        print(f"Setor {nave}: Escaneado e seguro")

print()

print("Varredura encerrada!")
