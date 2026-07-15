lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b # concatenando listas

print(lista_c)
lista_a.extend(lista_b) # Utilizando o extend não é possível fazer uma nova 
# variável, porque essa variável vai ser None, é necessário fazer diretamente
# com as variáveis existentes, neste caso você vai extender a lista a juntando
# com a lista b. 
print(lista_a)