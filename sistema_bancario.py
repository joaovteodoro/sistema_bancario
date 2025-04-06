# JOÃO VÍTOR TEODORO SANTOS
# 03/04/2025

import datetime

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
numero_transacao = 0
LIMITE_TRANSACAO = 10
dia_de_amanha = datetime.datetime.now().date() + datetime.timedelta(days=1)

while True:
    data_atual = datetime.datetime.now()

    print()
    print(menu)
    opcao = input("Escolha:")
    opcao = opcao.lower()

    if data_atual.date() >= dia_de_amanha:
        numero_transacao = 0
        dia_de_amanha = datetime.datetime.now().date() + datetime.timedelta(days=1)

    if opcao == "d":
        valor_deposito = 0

        try:
            valor_deposito = float(input("Digite o valor do depósito: "))
        except ValueError:
            print("Valor inválido!")  
            continue  

        if valor_deposito < 0:
            print("Não é possível depositar um valor negativo!")
        elif numero_transacao >= LIMITE_TRANSACAO:
            print(f"Você já atingiu o limite de {LIMITE_TRANSACAO} transações diárias!")
        else:    
            saldo += valor_deposito
            extrato.append(f"DEPÓSITO: R$ {valor_deposito:.2f} - {data_atual.strftime("%d/%m/%Y %H:%M")}")
            numero_transacao +=1

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
            print(f"Você já atingiu o limite de {LIMITE_SAQUE} saques diários!")    
        elif numero_transacao >= LIMITE_TRANSACAO:
            print(f"Você já atingiu o limite de {LIMITE_TRANSACAO} transações diárias!")
        else:
            saldo -= valor_saque
            extrato.append(f"SAQUE: R$ {valor_saque:.2f} - {data_atual.strftime("%d/%m/%Y %H:%M")}")
            numero_saque += 1
            numero_transacao +=1

            print()
            print("Operação confirmada!")
            print(f"Saque no valor de R$ {valor_saque:.2f} realizado.")
            print(f"SALDO: R$ {saldo:.2f}")

    elif opcao == "e":
        print("-" * 21 + " EXTRATO " + "-" * 21)
        print()

        for operacao in extrato:
            descricao, data = operacao.split(" - ") 
            print(descricao.ljust(30) + data.rjust(20))

        print()
        print(f"SALDO: R$ {saldo:.2f}")
        print("-" * 51)
        print()

    elif opcao == "q":
        print("Obrigado pela confiança!")
        break

    else:
        print("Digite uma opção válida!")    
