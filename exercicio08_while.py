# iterando strings com  while

nome = "David Rocha"

tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)

# mostrar = "*D*a*v*i*d* *R*o*c*h*a*

contador = 0
nome_novo = ""
while contador < tamanho_nome:
    letra = nome[contador]
    nome_novo += f"*{letra}"
    contador += 1

print(nome_novo)
    
# meu jeito

contador_2 = 0
while contador_2 < tamanho_nome:
    print(f"*{nome[contador_2]}", end="")
    contador_2 += 1
    
print()
