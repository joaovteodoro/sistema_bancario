# JOÃO VÍTOR TEODORO SANTOS
# 03/04/2025

menu = """========== MENU ==========
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
==========================
"""
saldo = 0
extrato = []
numero_saque = 0
LIMITE_SAQUE = 3


while True:
    print()
    print(menu)
    opcao = input("Escolha:")
    opcao = opcao.lower()

    if opcao == "d":
        valor_deposito = 0

        try:
            valor_deposito = float(input("Digite o valor do depósito: "))
        except ValueError:
            print("Valor inválido!")  
            continue  

        if valor_deposito < 0:
            print("Não é possível depositar um valor negativo!")
        else:    
            saldo += valor_deposito
            extrato.append(f"DEPÓSITO: R$ {valor_deposito:.2f} ")

            print()
            print("Operação confirmada!")
            print(f"Depósito no valor de R$ {valor_deposito:.2f} realizado.")
            print(f"SALDO: R$ {saldo:.2f}")

    elif opcao == "s":
        valor_saque = 0

        try:
            valor_saque = float(input("Digite o valor do saque: "))
        except ValueError:
            print("Valor inválido!")  
            continue 

        if valor_saque > 500:
            print("O valor limite por saque é de R$ 500,00")
        elif valor_saque > saldo:
            print("Saldo insuficiente!")
        elif numero_saque >= LIMITE_SAQUE:
            print("Você já atingiu o limite de 03 saques diários!")    
        else:
            saldo -= valor_saque
            extrato.append(f"SAQUE: R$ {valor_saque:.2f} ")
            numero_saque += 1

            print()
            print("Operação confirmada!")
            print(f"Saque no valor de R$ {valor_saque:.2f} realizado.")
            print(f"SALDO: R$ {saldo:.2f}")

    elif opcao == "e":
        print("-------- EXTRATO --------")
        print()

        for operacao in extrato:
            print(operacao)

        print()
        print(f"SALDO: R$ {saldo:.2f}")
        print("-" * 25)
        print()

    elif opcao == "q":
        print("Obrigado pela confiança!")
        break

    else:
        print("Digite uma opção válida!")    
