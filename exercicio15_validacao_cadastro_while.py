"""
2. Validação Completa de Cadastro

Objetivo: Simular a validação de um formulário de cadastro. O programa deve forçar 
o usuário a digitar dados válidos usando o while.

Regras:

Peça o Nome: O while deve continuar pedindo se o nome tiver menos de 3 caracteres (Dica: use len(nome)).

Peça a Idade: O while deve continuar pedindo se a idade não estiver entre 0 e 120 anos.

Peça o Salário: O while deve continuar pedindo se o salário for menor ou igual a zero.

Só quando todos os dados forem válidos, o programa exibe "Cadastro realizado com sucesso!" e mostra os dados na tela.
"""

validacao = "Digite Dados Válidos!"

print("Validação de Cadastro")

print()

nome_valido = False
idade_valido = False
salario_valido = False
while True:

    if not nome_valido:
        nome = input("Nome funcionário: ").title()

        if len(nome) > 3:
            nome_valido = True
        else:
            print(f"Nome inválido! {validacao}")
            continue

    else:
        nome_valido = True
        if not idade_valido:
            try:
                idade = int(input("Idade: "))

            except (ValueError, NameError):
                print(f"Digite somente números! {validacao}")
                continue

            if idade >= 0 and idade <= 120:
                idade_valido = True
            else:
                print(f"Idade incorreta, {validacao}")
                continue

        else:
            idade_valido = True
            if not salario_valido:
                try:
                    salario = float(input("Digite o salário do funcionário: R$ "))
                except ValueError:
                    print(f"Digite Valores válidos! {validacao}")
                    continue

                if salario > 0:
                    salario_valido = True
                else:
                    print(f"Salário incorreto, {validacao}")
                    continue
            else:
                print("Cadastro Realizado com sucesso!")
                break

print()

print(f"Cadastro de Funcionário: \n\nNome: {nome}\nIdade: {idade}\nSalário: R$ {salario:.2f}")




