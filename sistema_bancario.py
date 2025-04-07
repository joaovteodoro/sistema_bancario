# JOÃO VÍTOR TEODORO SANTOS
# 06/04/2025


import datetime
import re
from validate_docbr import CPF

saldo = 0
extrato = []
usuarios = []
numero_saque = 0
LIMITE_SAQUE = 3
AGENCIA = "0001"
contas = []

def menu ():
    
    menu = """========== MENU ==========
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
==========================
"""
    print()
    print(menu)
    opcao = input("Escolha:")
    opcao = opcao.lower()
    return opcao

def depositar(extrato,/):

    valor_deposito = 0
    global saldo

    try:
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito < 0:
         print("Não é possível depositar um valor negativo!")
        else:    
            saldo += valor_deposito
            extrato.append(f"DEPÓSITO: R$ {valor_deposito:.2f} - {data_atual.strftime("%d/%m/%Y %H:%M")}")

            print()
            print("Operação confirmada!")
            print(f"Depósito no valor de R$ {valor_deposito:.2f} realizado.")
            print(f"SALDO: R$ {saldo:.2f}")

    except ValueError:
        print("Valor inválido!")  
        
def sacar(*, extrato = extrato, LIMITE_SAQUE = LIMITE_SAQUE):
    global saldo
    global numero_saque
    valor_saque = 0

    try:
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque > 500:
            print("O valor limite por saque é de R$ 500,00")
        elif valor_saque > saldo:
            print("Saldo insuficiente!")
        elif numero_saque >= LIMITE_SAQUE:
            print(f"Você já atingiu o limite de {LIMITE_SAQUE} saques diários!")    
        else:
            saldo -= valor_saque
            extrato.append(f"SAQUE: R$ {valor_saque:.2f} - {data_atual.strftime("%d/%m/%Y %H:%M")}")
            numero_saque += 1

            print()
            print("Operação confirmada!")
            print(f"Saque no valor de R$ {valor_saque:.2f} realizado.")
            print(f"SALDO: R$ {saldo:.2f}")

    except ValueError:
        print("Valor inválido!")  
        
def mostar_extrato(extrato):
    print("-" * 21 + " EXTRATO " + "-" * 21)
    print()

    for operacao in extrato:
        descricao, data = operacao.split(" - ") 
        print(descricao.ljust(30) + data.rjust(20))

    print()
    print(f"SALDO: R$ {saldo:.2f}")
    print("-" * 51)
    print()

def cadastrar_usuario():
    global usuarios

    
    cpf_digitado = input("Digite o CPF do novo usuário: ")
    cpf_digitado = re.sub(r'\D', '', cpf_digitado) #retira os caracteres que não são números do texto
    cpf = CPF()

    if not cpf.validate(cpf_digitado):
        print("CPF inválido!")
    elif cpf_digitado in [usuario["cpf"] for usuario in usuarios]:
        print("Usuário já cadastrado!")    
    else:
        
        print()
        print("Realize o cadastro das informações abaixo.")
        nome = input("Nome completo: ")
        data_de_nascimento = input ("Data de nascimento: ")
        logradouro = input("Lograduoro: ")
        numero = input("Numero: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        sigla_estado = input("Sigla do Estado: ")
        sigla_estado = sigla_estado.upper()

        endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{sigla_estado}"

        novo_usuario = {"cpf": cpf_digitado, "nome": nome, "data_de_nascimento": data_de_nascimento, "endereco": endereco}
        usuarios.append(novo_usuario)

        print("Usuário cadastrado com sucesso!")
 
def criar_conta(AGENCIA, numero_conta):
    global usuarios
    global contas

    cpf_digitado = input("Digite o CPF: ")
    cpf_digitado = re.sub(r'\D', '', cpf_digitado) #retira os caracteres que não são números do texto
    cpf = CPF()

    if not cpf.validate(cpf_digitado):
        print("CPF inválido!")
    elif cpf_digitado not in [usuario["cpf"] for usuario in usuarios]:
        print("Usuário não cadastrado. Favor cadastrar o usuário antes de realizar o cadastro da conta.")
    else:
        nova_conta = {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": cpf_digitado} 
        contas.append(nova_conta)

        print("Conta criada com sucesso!")

def listar_contas(contas):
    if contas:
        for conta in contas:
            print (conta)
    else:
        print("Nenhuma conta cadastrada!")        

while True:
    data_atual = datetime.datetime.now()

    opcao = menu()

    if opcao == "d":
        depositar(extrato)

    elif opcao == "s":
        sacar(extrato = extrato, LIMITE_SAQUE = LIMITE_SAQUE)

    elif opcao == "e":
        mostar_extrato(extrato)

    elif opcao == "nu":
        cadastrar_usuario()

    elif opcao == "nc":
        numero_conta = len(contas)+1
        criar_conta(AGENCIA,numero_conta)

    elif opcao == "lc":
        listar_contas(contas) 
           
    elif opcao == "q":
        print("Obrigado pela confiança!")
        break

    else:
        print("Digite uma opção válida!")    
