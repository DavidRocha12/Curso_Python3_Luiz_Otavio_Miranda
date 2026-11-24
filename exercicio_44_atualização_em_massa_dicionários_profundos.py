"""
Atualização em Massa (Dicionários Profundos)

Você tem um dicionário com dados de usuários cadastrados em 
um sistema. Todos os usuários que estiverem com o plano "Basico" 
vão ganhar um upgrade gratuito e ter seus limites dobrados.

O que você deve fazer:

Percorra o dicionário usuarios. Se o plano do usuário for 
"Basico", altere o valor da chave "plano" para "Pro" e multiplique 
o "limite_gb" por 2 diretamente no dicionário original.

"""

usuarios = {
    "user_01": {"nome": "Rafael", "plano": "Basico", "limite_gb": 10},
    "user_02": {"nome": "Juliana", "plano": "Pro", "limite_gb": 50},
    "user_03": {"nome": "Marcos", "plano": "Basico", "limite_gb": 15}
}

for usuario, planos in usuarios.items():
    plano = planos["plano"]
    limite = planos["limite_gb"]
    if plano == "Basico":
        planos.update(plano="Pro", limite_gb=limite * 2)

print(usuarios)



# Resultado esperado ao dar print(usuarios):
# {
#     'user_01': {'nome': 'Rafael', 'plano': 'Pro', 'limite_gb': 20},
#     'user_02': {'nome': 'Juliana', 'plano': 'Pro', 'limite_gb': 50},
#     'user_03': {'nome': 'Marcos', 'plano': 'Pro', 'limite_gb': 30}
# }

