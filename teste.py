string = '1000' #– Este valor é imutável, você não consegue mudar ele

outra_variavel = f'{string[:3]}ABC{string[4:]}' # é possível modificar criando outra variável

print(string)

print(outra_variavel)

print(string.zfill(10))# - .zfill() é um método da string, ele coloca o total de caracteres nesse caso com 10 caracteres, como .upper(), .lower(), .isnumeric() etc …
