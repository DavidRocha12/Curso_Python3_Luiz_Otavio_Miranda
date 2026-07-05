"""
Range + For para usar intervalos de números

Estrutura da função range, mostrando os parâmetros que ele recebe:

range(start, stop, step)

o Step é para propor de quantos em quantos números deseja pular.

mas ele pode receber apenas um parâmetro, por exemplo o parâmetro de stop, que vai definir
a parada, e o start vira 0 e o step vira 1, veja o código abaixo: 
"""

for n in range(10):
    print(n)

"""
Resultado:

0
1
2
3
4
5
6
7
8
9
"""

for n in range(0, 10, 1):
    print(n)

"""
Range utilizando os três parâmetro vai agir do mesmo jeito que 
o primeiro exemplo.
Resultado:

0
1
2
3
4
5
6
7
8
9
"""
for n in range(0, -10, -1):
    print(n)
"""
utilizando range para contar números de traz para frente

Resultado:

0
-1
-2
-3
-4
-5
-6
-7
-8
-9
"""
for n in range(0, 10, 2):
    print(n)

"""
range iterando a contagem de 2 em 2 com o step.
resultado:

0
2
4
6
8
"""
