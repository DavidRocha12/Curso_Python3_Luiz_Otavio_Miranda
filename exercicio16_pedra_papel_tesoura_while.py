"""
3. Jogo do "Pedra, Papel e Tesoura" (Melhor de 3)
Objetivo: Criar um jogo de Jokenpô contra o computador que só acaba quando o jogador ou o computador conseguir 3 vitórias.

Regras:

Você vai precisar importar a biblioteca random para o computador escolher (import random).

Use duas variáveis contadoras: vitorias_jogador = 0 e vitorias_computador = 0.

O while deve rodar enquanto vitorias_jogador < 3 and vitorias_computador < 3.

Dentro do loop, o usuário escolhe (Pedra, Papel ou Tesoura) e o computador escolhe aleatoriamente.

Use if/elif/else para determinar quem ganhou a rodada e some +1 no contador do vencedor.

Ao final do loop, verifique quem chegou a 3 vitórias e declare o Grande Campeão.

Escolha um para começar, monte a sua lógica com calma (lembrando de usar o try/except onde achar necessário para o programa não quebrar)
 e mande aqui para darmos uma olhada!
"""

import random

print("Jogo de Jokenpô\n")
print("Escolha:\n1- Pedra\n2- Papel\n3- Tesoura\n")

vitorias_jogador = 0
vitorias_computador = 0

while vitorias_jogador < 3 and vitorias_computador < 3:
	try:
		jogador = int(input("Escolha uma das opções acima: "))
		
	except ValueError:
		print("Digite apenas números!")
		continue

	if jogador > 0 and jogador <= 3:
		computador = random.randint(1, 3)
		
		if jogador == 1 and computador == 3:
			print(f"Jogador escolheu {jogador}- Pedra, Computador escolheu {computador}- Tesoura")
			print("jogador ganhou essa rodada!")
			vitorias_jogador += 1
		elif jogador == 3 and computador == 1:
			print(f"Jogador escolheu {jogador}- Tesoura, Computador escolheu {computador}- Pedra")
			print("Computador ganhou essa rodada!")
			vitorias_computador += 1
		elif jogador == 3 and computador == 2:
			print(f"Jogador escolheu {jogador}- Tesoura, Computador escolheu {computador}- Papel")
			print("jogador ganhou essa rodada!")
			vitorias_jogador += 1
		elif jogador == 2 and computador == 3:
			print(f"Jogador escolheu {jogador}- Papel, Computador escolheu {computador}- Tesoura")
			print("Computador ganhou essa rodada!")
			vitorias_computador += 1
		elif jogador == 2 and computador == 1:
			print(f"Jogador escolheu {jogador}- Papel, Computador escolheu {computador}- Pedra")
			print("jogador ganhou essa rodada!")
			vitorias_jogador += 1
		elif jogador == 1 and computador == 2:
			print(f"Jogador escolheu {jogador}- Pedra, Computador escolheu {computador}- papel")
			print("Computador ganhou essa rodada!")
			vitorias_computador += 1
		else:
			if jogador == 1 and computador == 1:
				escolha = "Pedra"
			elif jogador == 2 and computador == 2:
				escolha = "Papel"
			else:
				escolha = "Tesoura"
			print(f"Jogador escolheu {jogador}, e computador escolheu {computador}")
			print(f"Ambos escolheram o mesmo valor, que é {escolha}!")
			print("Ninguém ganhou pontuação.")
	else:
		print("Digite a opção correta!")
		continue

	print()

print(f"Placar: Jogador {vitorias_jogador} x {vitorias_computador} Computador")

if vitorias_jogador == 3:
	print("O Jogador é o Campeão!")
else:
	print("O Computador é o Campeão!")
	print("Treine mais!")