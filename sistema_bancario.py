# JOÃO VÍTOR TEODORO SANTOS
# 11/04/2025

import datetime
import re
from validate_docbr import CPF



class Endereco:
    def __init__(self, logradouro, numero, bairro, cidade, sigla_estado):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.sigla_estado = sigla_estado

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.bairro} - {self.cidade}/{self.sigla_estado}"
    
def _cadastrar_endereco():
    logradouro = input("Lograduoro: ")
    numero = input("Numero: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    sigla_estado = input("Sigla do Estado: ")
    sigla_estado = sigla_estado.upper()

    endereco = Endereco(logradouro, numero, bairro, cidade, sigla_estado)
    return endereco


class Usuario:
    def __init__(self, cpf, nome, data_de_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.endereco = endereco
        
    def __str__(self):
        usuario = {"cpf": self.cpf, "nome": self.nome, "data_de_nascimento": self.data_de_nascimento, "endereco": self.endereco}
        return str(usuario)

def cadastrar_usuario(cpf_digitado):
    global usuarios
    
    cpf_digitado = cpf_digitado
    print(f"CPF do novo usuário: {cpf_digitado}")
  

    if cpf_digitado in [usuario.cpf for usuario in usuarios]:
        print("Usuário já cadastrado!")    
    else:
    
        nome = input("Nome completo: ")
        data_de_nascimento = input ("Data de nascimento: ")
        endereco = _cadastrar_endereco()

        novo_usuario = Usuario(cpf_digitado, nome, data_de_nascimento, endereco)
        usuarios.append(novo_usuario)

        print("Usuário cadastrado com sucesso!")
        print()


class Conta:
    LIMITE_SAQUE = 3
    numero_saque = 0

    def __init__(self, numero_conta, cpf, nome):
        self.AGENCIA = "0001"
        self.numero_conta = numero_conta
        self._saldo = 0
        self.cpf = cpf
        self.nome = nome
        self.extrato = []
        self.numero_saque = 0

    def criar_conta(self):
        return {"agencia": self.AGENCIA, "numero_conta": self.numero_conta, "cpf": self.cpf, "nome": self.nome} 
         
    
    def depositar(self):

        valor_deposito = 0

        try:
            valor_deposito = float(input("Digite o valor do depósito: "))
            if valor_deposito < 0:
                print("Não é possível depositar um valor negativo!")
            else:    
                self._saldo += valor_deposito
                self.extrato.append(f"DEPÓSITO: R$ {valor_deposito:.2f} - {data_atual.strftime("%d/%m/%Y %H:%M")}")

                print()
                print("Operação confirmada!")
                print(f"Depósito no valor de R$ {valor_deposito:.2f} realizado.")
                print(f"SALDO: R$ {self._saldo:.2f}")

        except ValueError:
            print("Valor inválido!")  

            
    def sacar(self):

        valor_saque = 0

        try:
            valor_saque = float(input("Digite o valor do saque: "))
            if valor_saque > 500:
                print("O valor limite por saque é de R$ 500,00")
            elif valor_saque > self._saldo:
                print("Saldo insuficiente!")
            elif self.numero_saque >= self.LIMITE_SAQUE:
                print(f"Você já atingiu o limite de {self.LIMITE_SAQUE} saques diários!")    
            else:
                self._saldo -= valor_saque
                self.extrato.append(f"SAQUE: R$ {valor_saque:.2f} - {data_atual.strftime("%d/%m/%Y %H:%M")}")
                self.numero_saque += 1

                print()
                print("Operação confirmada!")
                print(f"Saque no valor de R$ {valor_saque:.2f} realizado.")
                print(f"SALDO: R$ {self._saldo:.2f}")

        except ValueError:
            print("Valor inválido!")  


    def mostar_extrato(self):
        print("-" * 21 + " EXTRATO " + "-" * 21)
        print()

        for operacao in self.extrato:
            descricao, data = operacao.split(" - ") 
            print(descricao.ljust(30) + data.rjust(20))

        print()
        print(f"SALDO: R$ {self._saldo:.2f}")
        print("-" * 51)
        print()

    def listar_conta(self):
        print('-----------')  
        print(f"{self.nome.upper()}   (CPF: {self.cpf})")
        print(f"Conta: {self.numero_conta}  -  Agência: {self.AGENCIA}")  
        print()
        return ""

def cadastrar_conta(cpf_digitado):
    global usuarios
    global contas

    cpf_digitado = cpf_digitado
    print(f"CPF da conta: {cpf_digitado}")
    
    if cpf_digitado not in [usuario.cpf for usuario in usuarios]:
        print("Usuário não cadastrado. Favor cadastrar o usuário antes de realizar o cadastro da conta.")
    else:

        for usuario in usuarios:
            if usuario.cpf == cpf_digitado:
                nome = usuario.nome
                
        usuario = cpf_digitado
        numero_conta = len(contas)+1
        nova_conta = Conta(numero_conta, usuario, nome)
        contas.append(nova_conta)

        print("Conta criada com sucesso!")
        print(f"Conta: {nova_conta.criar_conta()}")

def filtrar_contas(cpf_digitado):
    global contas
    contas_usuario = []
    for conta in contas:
        if cpf_digitado == conta.cpf:
            contas_usuario.append(conta)
    return contas_usuario


def menu_conta(cpf_digitado):

    while True:

        print()
        print("========== MENU ========== \n" \
              "[e] Entrar conta \n" \
              "[a] Abrir conta \n" \
              "[lc] Listar TODAS as contas \n" \
              "[q] Sair \n" \
              "========================== \n" )
    

        opcao_entrada = input("Digite uma opção: ")
        opcao_entrada = opcao_entrada.lower()
  

        if opcao_entrada == "e":
            contas_usuario = filtrar_contas(cpf_digitado)
            numero_digitado = input("Digite a sua conta: ")

            try:
                numero_digitado = int(numero_digitado)
            except ValueError: 
                print("CONTA INVÁLIDA")
                return None

            conta_escolhida = None
            for conta in contas_usuario:
                if conta.numero_conta == numero_digitado:
                    conta_escolhida = conta
                    break

            if cpf_digitado not in [usuario.cpf for usuario in usuarios]:
                print("Usuário não cadastrado!")    
                print()
                print("CADASTRAR USUÁRIO:")
                cadastrar_usuario(cpf_digitado)
                return None
            elif not conta_escolhida:  
                print()
                print("CONTA INVÁLIDA!")
                print()
                return None
            else:   
                print("LOGIN REALIZADO!")

                return cpf_digitado, conta_escolhida  
            

        elif opcao_entrada == "a":

            if cpf_digitado not in [usuario.cpf for usuario in usuarios]:
                print("Usuário não cadastrado!")    
                print()
                print("CADASTRAR USUÁRIO:")
                cadastrar_usuario(cpf_digitado)
                print()
                
           
            print("CADASTRANDO CONTA...")
            cadastrar_conta(cpf_digitado)  
            continue
        
        elif opcao_entrada == "lc":
            listar_contas(contas) 
            continue
            
        elif opcao_entrada == "q":
            print("Obrigado pela confiança!")
            return "break"

        else:
            print("DIGITE UMA OPÇÃO VÁLIDA!")
            continue

def menu_operacoes(cpf, conta):
  while True:
    menu = " ========== MENU ========== \n " \
           "[d] Depositar \n " \
           "[s] Sacar \n " \
           "[e] Extrato \n " \
           "[q] Sair \n " \
           "[lc] Listar Contas USUÁRIO \n " \
           "=========================="

    print()
    print(menu)
    opcao = input("Escolha:")
    opcao = opcao.lower()

    if opcao == "d":
        conta.depositar()

    elif opcao == "s":
        conta.sacar()

    elif opcao == "e":
        conta.mostar_extrato()

    elif opcao == "lc":
        for conta in contas:
            if cpf == conta.cpf:
                print(conta.listar_conta())
        
    elif opcao == "q":
        print("ENCERRANDO OPERAÇÃO!")
        break
    else:
        print("Digite uma opção válida!")    

def listar_contas(contas): 
    if contas:
        for conta in contas:
            print (conta.listar_conta())
    else:
        print("Nenhuma conta cadastrada!")        


usuarios = []
contas = []

while True:
    data_atual = datetime.datetime.now()

    print()
    cpf_digitado = input("Digite o seu CPF: ")
    cpf_digitado = re.sub(r'\D', '', cpf_digitado) #retira os caracteres que não são números do texto
    cpf = CPF()

    if not cpf.validate(cpf_digitado):
        print("CPF inválido!")
        print()
        continue
    
    print()


    resultado_menu = menu_conta(cpf_digitado) 

    if resultado_menu is None:
        continue
    elif resultado_menu is "break":
        break
    else:
        cpf, conta = resultado_menu

    menu_operacoes(cpf, conta)    





