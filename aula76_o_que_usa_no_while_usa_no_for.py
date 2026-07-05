"""
O que aprendemos com o while também funciona no for(continue, break, else, etc)
"""

for i in range(10):
    if i == 2:
        print("i é 2, pulando...")
        continue

    if i == 8:
        print("i é 8, seu else não executará")
        break

    for j in range(1, 3):
        print(i, j)

else:
    print("For completo com sucesso!")

"""
resultado:

0 1
0 2
1 1
1 2
i é 2, pulando...
3 1
3 2
4 1
4 2
5 1
5 2
6 1
6 2
7 1
7 2
i é 8, seu else não executará
"""
