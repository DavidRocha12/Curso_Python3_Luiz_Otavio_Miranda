"""Calculadora com while"""


print("Calculadora\n")

while True:
    n_1 = input("Digite um número: ")
    n_2 = input("Digite outro número: ")

    print()
    valor = None
    try:
        n_1 = int(n_1)
        n_2 =int(n_2)

        valor = True

        print("\nEscolha o calculo: \n + Soma\n - Subtração\n * Multiplicação\n / Divisão\n")

        escolha = input("Digite qual cálculo deseja fazer: ")

        if escolha not in "+-*/":
            print("Operador invalido!\n")
            continue

        if escolha ==  "+":
            print(n_1 + n_2)
        elif escolha == "-":
            if n_2 > n_1:
                print(n_2 - n_1)
            else:
                print(n_1 - n_2)
        elif escolha == "*":
            print(n_1 * n_2)
        elif escolha == "/":
            print(int(n_1 / n_2))
        else: 
            print("Escolha um dos quatro simbolos acima!\n")
        
        cont = input("\nQuer continuar? S / N ")

        print()

        if cont in "Nn":
            print("saindo...")
            break
    except:
        print()
        print("isso não é um número!\n")
