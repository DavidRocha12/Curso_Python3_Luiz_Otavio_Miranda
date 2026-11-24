"""
Boletim de Notas (Dicionários Aninhados)

Este é um clássico. Você tem um dicionário onde cada 
chave é um aluno. O valor desse aluno é outro dicionário 
contendo as matérias e as notas.

O que você deve fazer:
Crie um novo dicionário chamado medias. Calcule a média geral 
de cada aluno e guarde neste novo dicionário.

Dica: O método .values() pode ser muito útil para pegar apenas 
os números das notas na hora de somar.
"""

boletim = {
    "Lucas": {"Matematica": 8.0, "Historia": 7.5, "Geografia": 9.0},
    "Mariana": {"Matematica": 9.5, "Historia": 8.0, "Geografia": 8.5},
    "Pedro": {"Matematica": 5.0, "Historia": 6.5, "Geografia": 7.0}
}

media = {}
for aluno, valor in boletim.items():
	notas = valor.values()
	md = sum(notas) / len(valor)
	media[aluno] = float(f"{md:.2f}")

print(media)
