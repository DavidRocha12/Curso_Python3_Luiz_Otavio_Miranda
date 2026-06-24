"""
2. O Caixa Eletrônico (Menu Interativo)
Objetivo: Simular um caixa eletrônico onde o usuário pode sacar, depositar ou sair.

Regras:

Comece com um saldo de R$ 500.

Use um while True (loop infinito) que só para quando uma variável booleana sistema_ativo se tornar False (ou usando break).

Exiba um menu: [1] Ver Saldo, [2] Depositar, [3] Sacar, [4] Sair.

No saque, use condicionais para garantir que o usuário não saque mais do que tem disponível.

"""

sistema_ativo = True
saldo = 500.0
while sistema_ativo:
    print("[1] Ver Saldo\n[2] Depositar\n[3] Sacar\n[4] Sair\n")
    try:
        escolha = input("Digite a opção desejada: ")
        escolha = int(escolha)

        print()
    
    except ValueError:
        print("Digite a opção correta!")
        continue

    if escolha == 1:
        print(f"Saldo = R$ {saldo:.2f}")
    elif escolha == 2:
        deposito = float(input("Digite o valor a ser depositado: R$ "))
        if deposito > 0:
            saldo += deposito
            print("Deposito feito com sucesso!")
        else:
            print("Valor do deposito invalido!")
    elif escolha == 3:
        saque = float(input("Digite o valor a sacar: R$ "))
        if saldo > 0 and saque <= saldo:
            saldo -= saque
            print("Saque realizado com sucesso!")
        elif saque > saldo or saldo == 0:
            print("Saldo insuficiente")
    elif escolha == 4:
        sistema_ativo = False
    else:
        print("Opção inexistente no menu!")
        
    print()

